import input

custom_fields = [
    input.OverSpecifiedField(['spec', 'statefulSet'], used_fields=[
        ['spec', 'statefulSet', 'spec', 'serviceName'],
    ]),
]