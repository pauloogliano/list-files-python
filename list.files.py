# ========================
# Created by 3P[0]. ;)
#
#        %%%%%%%%%
#        %%    %%
#             %%
#          %%   %%
#       %% %%    %%
#       %% %%   %%
#         %%%%%%
#          %%
#          %%
#
# ========================

from glob import glob

path           = '' # set the path here
directoryPath  = path + "*."
fileExtensions = ["PHP"]
listOfFiles    = []

for extension in fileExtensions:
	listOfFiles.extend(glob(directoryPath + extension))

for file in listOfFiles:
	print("- Listando arquivos -")
	print(file)