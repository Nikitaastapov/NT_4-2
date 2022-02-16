import os
path = os.getcwd()
files = os.listdir(path)
file_path_new = os.path.join(path, 'result.doc')

def add_list(list_files=[]):
    for i in files:
        if 'txt' in i:
            file_path = os.path.join(path, i)
            with open (file_path) as f:
                temp_lst = []
                line_nmb = len(f.readlines())
                temp_lst.append(line_nmb)
                temp_lst.append(i)
                list_files.append(temp_lst)
    return sorted(list_files)
            

def get_inf():
   for k in add_list():
        line_nmb = k[0]
        file_nm = k[1]
        print(line_nmb, file_nm) 
        add_inf_to_file (line_nmb, file_nm)
    
        

def add_inf_to_file (str_nm, file_name): 
    file_path = os.path.join(path, file_name) 
    with open(file_path_new, "a") as new_file:
        text = file_name +'\n'
        new_file.write(text)
        text = str(str_nm) +'\n'
        new_file.write(text)
        with open(file_path, "r") as read_file:
            for line in read_file:
                new_file.write(str(line))
          
    
    

get_inf()

