import sys

import mediafiregrabber

downloaded_resources_folder = sys.argv[1]

mediafiregrabber.download("https://www.mediafire.com/folder/8t7wsdvzdzazx/pycraft_resources", save=downloaded_resources_folder)