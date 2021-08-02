import bpy
import json

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\PSIRT\\PSIRT.json') as f:
    PSIRT = json.load(f)

print(PSIRT)
for count, item in enumerate(PSIRT, start=1):
    if count <= 9:
        if float(item[11]) >= 9:
            bpy.data.objects['Spotlight.00%s' % count].data.color = (1.0,0.0,0.0)
            bpy.data.objects['CVE_Score_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5']
            bpy.data.objects['CVE_Score_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryTitle_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']            
            bpy.data.objects['AdvisoryTitle_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5']
            bpy.data.objects['Eyes.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5']
            bpy.data.objects['BugID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['BugID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_5']            
        elif float(item[11]) <= 8.9 and float(item[11]) >= 7:
            bpy.data.objects['Spotlight.00%s' % count].data.color = (1.0,0.25,0.0)
            bpy.data.objects['CVE_Score_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4']
            bpy.data.objects['CVE_Score_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryTitle_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryTitle_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4']
            bpy.data.objects['Eyes.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4']            
            bpy.data.objects['BugID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['BugID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_4']
        elif float(item[11]) <= 6.9 and float(item[11]) >= 5:
            bpy.data.objects['Spotlight.00%s' % count].data.color = (1.0,1.0,0.0)
            bpy.data.objects['CVE_Score_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3']
            bpy.data.objects['CVE_Score_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryTitle_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryTitle_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3']
            bpy.data.objects['Eyes.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3']
            bpy.data.objects['BugID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['BugID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_3']            
        elif float(item[11]) <= 4.9 and float(item[11]) >= 3:
            bpy.data.objects['Spotlight.00%s' % count].data.color = (1.0,1.0,0.25)
            bpy.data.objects['CVE_Score_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2']
            bpy.data.objects['CVE_Score_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryTitle_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryTitle_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2']
            bpy.data.objects['Eyes.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2']
            bpy.data.objects['BugID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['BugID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_2']            
        else:
            bpy.data.objects['Spotlight.00%s' % count].data.color = (1.0,1.0,1.0)
            bpy.data.objects['CVE_Score_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1']
            bpy.data.objects['CVE_Score_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryTitle_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryTitle_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1']
            bpy.data.objects['Eyes.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1']
            bpy.data.objects['BugID_Label.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['BugID_Value.00%s' % count].material_slots[0].material = bpy.data.materials['Score_1']            
    else:
        if float(item[11]) >= 9:
            bpy.data.objects['Spotlight.0%s' % count].data.color = (1.0,0.0,0.0)
            bpy.data.objects['CVE_Score_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5']
            bpy.data.objects['CVE_Score_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5']
            bpy.data.objects['BugID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5_Text']
            bpy.data.objects['BugID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_5']            
        elif float(item[11]) <= 8.9 and float(item[11]) >= 7:
            bpy.data.objects['Spotlight.0%s' % count].data.color = (1.0,0.25,0.0)
            bpy.data.objects['CVE_Score_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4']
            bpy.data.objects['CVE_Score_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4']            
            bpy.data.objects['BugID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4_Text']
            bpy.data.objects['BugID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_4']
        elif float(item[11]) <= 6.9 and float(item[11]) >= 5:
            bpy.data.objects['Spotlight.0%s' % count].data.color = (1.0,1.0,0.0)
            bpy.data.objects['CVE_Score_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3']
            bpy.data.objects['CVE_Score_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3']
            bpy.data.objects['BugID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3_Text']
            bpy.data.objects['BugID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_3']            
        elif float(item[11]) <= 4.9 and float(item[11]) >= 3:
            bpy.data.objects['Spotlight.0%s' % count].data.color = (1.0,1.0,0.25)
            bpy.data.objects['CVE_Score_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2']
            bpy.data.objects['CVE_Score_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2']
            bpy.data.objects['BugID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2_Text']
            bpy.data.objects['BugID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_2']            
        else:
            bpy.data.objects['Spotlight.0%s' % count].data.color = (1.0,1.0,1.0)
            bpy.data.objects['CVE_Score_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1']
            bpy.data.objects['CVE_Score_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['AdvisoryTitle_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1']
            bpy.data.objects['BugID_Label.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1_Text']
            bpy.data.objects['BugID_Value.0%s' % count].material_slots[0].material = bpy.data.materials['Score_1']            