from abc import abstractmethod

from myChecks.checkov.common.checks.base_check import BaseCheck
from myChecks.checkov.cloudformation.checks.resource.registry import resource_registry


class BaseResourceCheck(BaseCheck):
    def __init__(self, name, id, categories, supported_resources):
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources,
                         block_type="resource")
        self.supported_resources = supported_resources
        resource_registry.register(self)

    @abstractmethod
    def scan_resource_conf(self, conf):
        raise NotImplementedError()

    def scan_entity_conf(self, conf):
        return self.scan_resource_conf(conf)
