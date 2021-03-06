from myChecks.checkov.common.models.enums import CheckResult, CheckCategories
from myChecks.checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class AzureInstancePassword(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Azure Instance does not use basic authentication(Use SSH Key Instead)"
        id = "CKV_AZURE_1"
        supported_resources = ['azurerm_virtual_machine']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for password configuration at azure_instance:
            https://www.terraform.io/docs/providers/azure/r/instance.html
        :param conf: azure_instance configuration
        :return: <CheckResult>
        """
        if 'os_profile_linux_config' in conf.keys():
            linux_config = conf['os_profile_linux_config'][0]
            if 'disable_password_authentication' in linux_config.keys():
                disable_password_authentication = linux_config['disable_password_authentication']
                if disable_password_authentication == [False]:
                    return CheckResult.FAILED
        return CheckResult.PASSED


check = AzureInstancePassword()
