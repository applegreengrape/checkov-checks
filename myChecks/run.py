#!/usr/bin/env python

from myChecks.checkov.cloudformation.runner import Runner as cfn_runner
from myChecks.checkov.common.runners.runner_registry import RunnerRegistry
from myChecks.checkov.common.util.docs_generator import print_checks
from myChecks.checkov.terraform.runner import Runner as tf_runner
from myChecks.checkov.version import version

def run():
    runner_registry = RunnerRegistry(tf_runner(), cfn_runner())
    scan_reports = runner_registry.run('.')
    runner_registry.print_reports_default(scan_reports)

if __name__ == '__main__':
    run()