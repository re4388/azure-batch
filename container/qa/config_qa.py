#-------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
#--------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_containers.py "

_BATCH_ACCOUNT_NAME = 'batch0615'
_BATCH_ACCOUNT_KEY = 'kn+19hlsKJCjJNDhF06fEhg0XSBRIf7+brx1hokmWlmhIyjK7M5R1j0FFLI6imRqam9s5mmjnVNmtvCdIF+sdw=='
_BATCH_ACCOUNT_URL = 'https://batch0615.southcentralus.batch.azure.com'

_REGISTRY_SERVER = 'cr0615.azurecr.io'
_REGISTRY_USER_NAME = 'cr0615'
_REGISTRY_PASSWORD = 'c1MwqFSWMZGZ=I/etTdVYOczcLzhG9ND'

_DOCKER_IMAGE = 'cr0615.azurecr.io/cr0615/qa:0.0.01beta'

_POOL_NODE_COUNT = 1 # Pool node count
# _POOL_VM_SIZE = 'STANDARD_A1_v2' # VM Type/Size
_POOL_VM_SIZE = 'STANDARD_D3_V2' # VM Type/Size
# _POOL_VM_SIZE = 'Standard_NC24s_v2' # VM Type/Size
_POOL_ID = 'ContainersPoolqa6' # Your Pool ID
_JOB_ID = 'ContainersJobqa6' # Job ID
_TASK_ID= 'ContainersTaskqa6' # Task ID

_STANDARD_OUT_FILE_NAME = 'stdout.txt' # Standard Output file
_STANDARD_ERR_FILE_NAME = 'stderr.txt' # Standard Error file