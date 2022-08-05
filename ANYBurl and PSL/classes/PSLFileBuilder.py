from classes.EntityConverter import EntityConverter
from classes.DatasetGenerator import DatasetGenerator

class PSLFileBuilder():
    def __init__(self, rels = None):
        if(rels is None):
            self.rels = []
        else:
            self.rels = rels

    def build_map_files(self, entity_converter, seperator = "%20"): 
      generator = DatasetGenerator()
      for relindex,name in entity_converter.relindex_to_name.items():
         
        f = open(f"data/{generator.encode_text(name)}_map.txt", "a",  encoding="utf-8")
        first_line = True
        items_added = []
        for h,r,t in  self.rels:
          if r == relindex and t not in items_added: #Avoid adding duplicates to the map
            items_added.append(t)
            t_map_name = generator.encode_text(entity_converter.entityindex_to_name[t])
            if first_line:
              f.write(f"{t}\t{t_map_name}")
              first_line = False
            else:
              f.write(f"\n{t}\t{t_map_name}")
        f.close()
        
    def build_obs_files(self):      
        for relindex,name in rel_indices.items():       
            f = open(f"data/{name}_obs.txt", "a")
            for h,r,t in rels:
                if r != relindex:
                    continue
            f.close()
            
        return
    
    def build_target_files(self):
        return
    
    def build_truth_files(self):
        return
    