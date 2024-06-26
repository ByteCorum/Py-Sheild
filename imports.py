import os

class ImportManager:

    def __init__(self,filePath) -> None:
        self.modules = []
        self.file = filePath
        self.GetImports()
        self.CheckImports()

    def GetImports(self):
        with open(self.file, "r") as f:
            
            for line in f:
                line = line.strip()
                if line.startswith("import") or line.startswith("from"):
                    module = line.split()[1]
                    index = module.find('.')
                    if index == -1 and not module in self.modules:
                        self.modules.append(module)
                    elif not index == -1 and not module[:index] in self.modules:
                        self.modules.append(module[:index])
    
    def CheckImports(self):
        imp = ""
        for module in self.modules:
            imp+="import "+str(module)+"\n"
        try:
            exec(imp)
        except Exception as importError:
            print(importError)
            os._exit(0)

    @property
    def imports(self):
        return self.modules


