from known_schemas import *

WHITEBOX = [
    K8sField(['spec', 'backup', 'pitr', 'resources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'backup', 'imagePullPolicy'], ImagePullPolicySchema),
    K8sField(['spec', 'backup', 'serviceAccountName'], ServiceAccountNameSchema),
    K8sField(['spec', 'haproxy', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'haproxy', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'haproxy', 'priorityClassName'], PriorityClassNameSchema),
    K8sField(['spec', 'haproxy', 'replicasServiceType'], ServiceTypeSchema),
    K8sField(['spec', 'haproxy', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'haproxy', 'resources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'replicasServiceType'], ServiceTypeSchema),
    K8sField(['spec', 'haproxy', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], StorageResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'sidecarResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'haproxy', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'haproxy', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'haproxy', 'size'], ReplicasSchema),
    K8sField(['spec', 'haproxy', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'logcollector', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'logcollector', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'proxysql', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'proxysql', 'priorityClassName'], PriorityClassNameSchema),
    K8sField(['spec', 'proxysql', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'proxysql', 'resources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'proxysql', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'proxysql', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'proxysql', 'size'], ReplicasSchema),
    K8sField(['spec', 'proxysql', 'volumeSpec', 'persistentVolumeClaim', 'resources'], StorageResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'pxc', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'pxc', 'imagePullPolicy'], ImagePullPolicySchema),
    K8sField(['spec', 'pxc', 'priorityClassName'], PriorityClassNameSchema),
    K8sField(['spec', 'pxc', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'pxc', 'resources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], StorageResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarResources'], ComputeResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'pxc', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'pxc', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'pxc', 'volumeSpec', 'persistentVolumeClaim', 'resources'], StorageResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'size'], ReplicasSchema),
]

BLACKBOX = [
    K8sField(['spec', 'backup', 'pitr', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'haproxy', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'haproxy', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'haproxy', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'sidecarResources'], ResourceRequirementsSchema),
    K8sField(['spec', 'haproxy', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'haproxy', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'haproxy', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'haproxy', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'logcollector', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'logcollector', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'proxysql', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'proxysql', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'proxysql', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarResources'], ResourceRequirementsSchema),
    K8sField(['spec', 'proxysql', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'proxysql', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'proxysql', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'proxysql', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'affinity', 'advanced'], AffinitySchema),
    K8sField(['spec', 'pxc', 'containerSecurityContext'], SecurityContextSchema),
    K8sField(['spec', 'pxc', 'podSecurityContext'], PodSecurityContextSchema),
    K8sField(['spec', 'pxc', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], ResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarResources'], ResourceRequirementsSchema),
    K8sField(['spec', 'pxc', 'sidecarVolumes', 'ITEM'], VolumeSchema),
    K8sField(['spec', 'pxc', 'sidecars', 'ITEM'], ContainerSchema),
    K8sField(['spec', 'pxc', 'tolerations'], TolerationsSchema),
    K8sField(['spec', 'pxc', 'volumeSpec', 'persistentVolumeClaim', 'resources'], ResourceRequirementsSchema),
]