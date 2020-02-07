

# Thia code is for GT project feature selection

input_file = 'RawData_ZERO.csv'

title_list = []

with open(input_file, 'r') as f:
    line = f.readline()
    title_list = line.strip('\n').split(',')
    
#for item in title_list:
#    print item
    

layout_dict = {}

index = 0
for feature in title_list:
    layout_dict[index] = feature
    index += 1
    

unique_dict = {}
total_counter = 0
with open(input_file, 'r') as f:

    for line in f:
        line_list = line.strip('\n').split(',')
        
        if line_list[0] != 'Restatement_Classifier':
        
            for i in range(len(line_list)):
                
                cur_feature = layout_dict[i]
                cur_val = line_list[i]
                
                if cur_feature not in unique_dict:
                    unique_dict[cur_feature] = set()
                
                unique_dict[cur_feature].add(cur_val)
                
            total_counter += 1

for feature in title_list:
    
    print feature, len(unique_dict[feature]), total_counter
            
    
    