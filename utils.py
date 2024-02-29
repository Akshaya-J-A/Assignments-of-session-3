from db import district_list

def create(dis):
    if district_list:
        dis['id']=max(district['id'] for district in district_list)+1
    else:
         dis['id'] = 1
    district_list.append(dis)
    print("Updated list:",district_list)
    
def retrieve(dis_id):
    for district in district_list:
        if district['id'] == dis_id:
            return district
    return None
    
    
def update(district_id,new_name):
     for district in district_list:
        if district['id'] == district_id:
            district['name'] = new_name
     print("Updated district list:", district_list)


def delete(dis_id):
    district_list[:] = [district for district in district_list if district['id'] != dis_id]
    print("Updated district list:", district_list)