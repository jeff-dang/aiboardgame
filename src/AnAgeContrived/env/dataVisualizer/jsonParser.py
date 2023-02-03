import json

class JSONParser:
  def __init__(self, jsonFile):
    self.jsonFile = jsonFile
    #self.jsonOutput = self.set_jsonOutput(self.jsonFile)
  
  def set_jsonFile(self, jsonFile):
      self.jsonFile = jsonFile

  def get_jsonFile(self):
      return self.jsonFile

  def get_jsonOutput(self):
        jsonFile = open(str(self.jsonFile),'r').read()
        jsonData = json.loads(jsonFile)
        return jsonData

  # def set_jsonOutput(self):
  #       jsonFile = open(str(self.jsonFile),'r').read()
  #       self.jsonOutput = json.loads(jsonFile)

  # def get_jsonOutput(self):
  #     return self.jsonOutput

p1 = JSONParser("tic-tac-toe_json.json")
#p1.get_jsonOutput()
print(p1.get_jsonOutput())

