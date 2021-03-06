#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os
from com.microsoft.azure.management.websites.models import SkuOptions, WorkerSizeOptions, DatabaseServerType

class CiStub(object):

    def getProperty(self, name):
        return self.__dict__[name]

    def setProperty(self, name, value):
        self.__dict__[name] = value



class SubscriptionCi(CiStub):

    def __init__(self):
        self.name = "MyAzureSubscription"
        self.id = "Infrastructure/%s" % self.name
        self.type = "azure.Subscription"
        self.subscriptionId = None
        self.tenantId = None
        self.clientId = None
        self.clientKey = None
        self.ftpUser = None
        self.ftpPassword = None
        self.azureBaseURL = "https://management.azure.com/"
        self.azureManagementURL = "https://management.core.windows.net/"
        self.azureActiveDirectoryURL = "https://login.windows.net/"
        self._init_from_file()

    def _init_from_file(self):
        file_location = os.getenv('azure_subscription_conf')
        if not file_location:
            raise Exception("No environment variable named 'azure_subscription_conf' set.")
        with open(file_location, 'r') as inf:
            settings = eval(inf.read())
            self.subscriptionId = settings["subscriptionId"]
            self.tenantId = settings["tenantId"]
            self.clientId = settings["clientId"]
            self.clientKey = settings["clientKey"]
            self.ftpUser = settings["ftpUser"]
            self.ftpPassword = settings["ftpPassword"]


class ResourceGroupCi(CiStub):

    def __init__(self):
        self.name = "MyAzureResource"
        self.id = "Infrastructure/MyAzureSubscription/%s" % self.name
        self.type = "azure.ResourceGroup"
        self.subscription = SubscriptionCi()
        self.resourceName = "xld_azure_app_service_plugin_tests2"
        self.resourceLocation = "westeurope"
        self.resourceTags = {'myTag': 'myTagValue'}


class AppServicePlanCi(CiStub):

    def __init__(self):
        self.name = "MyAppServicePlan"
        self.id = "Infrastructure/MyAzureSubscription/MyAzureResource/%s" % self.name
        self.type = "azure.AppServicePlan"
        self.servicePlanName = "xld_azure_app_service_plugin_basic_plan"
        self.location = "westeurope"
        self.sku = SkuOptions.Basic
        self.workerSize = WorkerSizeOptions.Small


class WebAppCi(CiStub):

    def __init__(self):
        self.name = "MyWebApp"
        self.id = "Infrastructure/MyAzureSubscription/MyAzureResource/%s" % self.name
        self.type = "azure.WebAppModule"
        self.appName = "xld-azure-app-service-plugin-webapp"
        self.plan = "xld_azure_app_service_plugin_basic_plan"
        self.appSettings = {"mykey": "myvalue"}
        self.sqlDatabaseConnectionStrings = {"mykey1": "myvalue"}
        self.sqlServerConnectionStrings = {"mykey2": "myvalue"}
        self.customConnectionStrings = {"mykey3": "myvalue"}
        self.platform32bit = True
        self.alwaysOn = False
        self.netFrameworkVersion = "v4.0"
        self.phpVersion = "5.6"
        self.pythonVersion = "2.7"
        self.javaVersion = "1.8.0_60"
        self.javaContainer = "TOMCAT"
        self.javaContainerVersion = "8.5.6"


class TriggeredWebJobCi(CiStub):

    def __init__(self):
        self.name = "MyWebJob"
        self.id = "Infrastructure/MyAzureSubscription/MyAzureResource/%s" % self.name
        self.type = "azure.TriggeredWebJobModule"
        self.webJobName = "xld-webjob"
        self.executableFileName = "echo.sh"
        self.appName = "xld-azure-app-service-plugin-webapp"
        self.schedule = "0 */10 * * * *"


class ContinuousWebJobCi(CiStub):

    def __init__(self):
        self.name = "MyContinuousWebJob"
        self.id = "Infrastructure/MyAzureSubscription/MyAzureResource/%s" % self.name
        self.type = "azure.ContinuousWebJobModule"
        self.webJobName = "xld-continuous-webjob"
        self.executableFileName = "echo.sh"
        self.appName = "xld-azure-app-service-plugin-webapp"
        self.isSingleton = False

