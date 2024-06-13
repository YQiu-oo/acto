import os

import yaml

from acto.kubectl_client.kubectl import KubectlClient


class OperatorApplicationPartitionFailure:
    """Simulate a network partition between the operator and the application"""

    def __init__(self, operator_selector: dict, app_selector: dict):
        self.operator_selector = operator_selector
        self.app_selector = app_selector

    def apply(self, kubectl_client: KubectlClient):
        """Apply the failure to the cluster"""
        failure_file = os.path.join("failures", self.name() + ".yaml")
        self.to_file(failure_file)
        kubectl_client.kubectl(
            ["apply", "-f", failure_file, "-n", "chaos-mesh"],
            capture_output=True,
        )
        kubectl_client.wait(
            failure_file,
            'jsonpath={.status.conditions[?(@.type=="AllInjected")].status}=True',
            timeout=600,
        )

    def cleanup(self, kubectl_client: KubectlClient):
        """Cleanup the failure from the cluster"""
        failure_file = os.path.join("failures", self.name() + ".yaml")
        kubectl_client.kubectl(
            ["delete", "-f", failure_file, "-n", "chaos-mesh", "--timeout=30s"],
            capture_output=True,
        )

    def name(self) -> str:
        """Get the name of the failure"""
        return "operator-application-partition"

    def to_dict(self) -> dict:
        """Dump the spec to a dict"""
        return {
            "apiVersion": "mesh.org/v1alpha1",
            "kind": "NetworkChaos",
            "metadata": {
                "name": "operator-application-partition",
            },
            "spec": {
                "action": "partition",
                "mode": "all",
                "selector": self.operator_selector,
                "direction": "both",
                "target": {
                    "mode": "all",
                    "selector": self.app_selector,
                },
            },
        }

    def to_file(self, file_path: str):
        """Write the spec to a file"""
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(self.to_dict(), f)
