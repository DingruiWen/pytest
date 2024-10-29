import yaml

f = open("../config/data.yaml")
data = yaml.safe_load(f)
print(data['hero'])