import os;
import json;
import pandas as pd;
import math
import numpy as np
import operator

openpose_kp_folder = "D:\\PhD\\Auburn\\CourseWork\\Deep_Learning\\Project\\Observational_exp\\AUBE_Lab\\keypoints\\neck_rotation";
file_path = 'D:\PhD\Auburn\CourseWork\Deep_Learning\Project\openpose-1.7.0-portable\openpose\images_keyPoints\standard_pose_image_keypoints.json';
vicon_file_path = 'D:\\PhD\\Auburn\\CourseWork\\Deep_Learning\\Project\\Observational_exp\\Vicon_keypoints\\Neck_Rotation.csv';
number_of_coordinates = 3;# one of these coordinates is confidence for OpenPose data.
number_of_keypoints = 25;
key_points_coordinates = [] #(x, y) coordinates

RSHO_col = 'Test1:RSHO'
RUPA_col = 'Test1:RUPA'
LSHO_col = 'Test1:LSHO'
LUPA_col = 'Test1:LUPA'

LASI_col = 'Test1:LASI'
RASI_col = 'Test1:RASI'

RANK_col = 'Test1:RANK'
LANK_col = 'Test1:LANK'

LHEE_col = 'Test1:LHEE'
RHEE_col = 'Test1:RHEE'

RKNE_col = 'Test1:RKNE'
LKNE_col = 'Test1:LKNE'

LELB_col = 'Test1:LELB'
RELB_col = 'Test1:RELB'



segments_list = [(3, 2), (5, 6), (9, 12), (9, 10), (11, 10), (24, 11), (14, 21), (14, 13), (12, 13), (7, 6), (3,4), (2, 5)];
vicon_segment_list = [(RSHO_col, RUPA_col), (LSHO_col, LUPA_col), (LASI_col ,RASI_col), (RASI_col, RKNE_col), (RKNE_col ,RANK_col), (RHEE_col ,RANK_col), (LHEE_col, LANK_col), (LKNE_col, LANK_col), (LASI_col, LKNE_col), (LELB_col, LUPA_col), (RELB_col, RUPA_col), (LSHO_col, RSHO_col)];
#vicon_segment_list_with_indices = [()]

def read_csv(vicon_file_path):
    vicon = pd.read_csv(vicon_file_path, skiprows = [0, 1, 3, 4])
    vicon = vicon.iloc[:, 2:]
    #print(vicon.iloc[2])
    #Vicon segment Indices
    RSHO_index_no = vicon.columns.get_loc(RSHO_col);
    LSHO_index_no = vicon.columns.get_loc(LSHO_col);
    RUPA_index_no = vicon.columns.get_loc(RUPA_col);
    LUPA_index_no = vicon.columns.get_loc(LUPA_col);
    RASI_index_no = vicon.columns.get_loc(RASI_col);
    LASI_index_no = vicon.columns.get_loc(LASI_col);
    RANK_index_no = vicon.columns.get_loc(RANK_col);
    LANK_index_no = vicon.columns.get_loc(LANK_col);
    RHEE_index_no = vicon.columns.get_loc(RHEE_col);
    LHEE_index_no = vicon.columns.get_loc(LHEE_col);
    RKNE_index_no = vicon.columns.get_loc(RKNE_col);
    LKNE_index_no = vicon.columns.get_loc(LKNE_col);
    RELB_index_no = vicon.columns.get_loc(RELB_col);
    LELB_index_no = vicon.columns.get_loc(LELB_col);
    
    #Fill NAN values with 100000. As Openpose has 0 for the kep points that are not detected we need to replace nan for vicon with something far from 0
    vicon = vicon.fillna(100000)
    #print(vicon.head().to_string())
    vicon_difference_df= pd.DataFrame()
    vicon_difference_df['RSHO-RUPA_x'] = vicon.iloc[:, RSHO_index_no] - vicon.iloc[:, RUPA_index_no]
    vicon_difference_df['RSHO-RUPA_y'] = vicon.iloc[:, RSHO_index_no+1] - vicon.iloc[:, RUPA_index_no+1]
    
    vicon_difference_df['LSHO-LUPA_x'] = vicon.iloc[:, LSHO_index_no] - vicon.iloc[:, LUPA_index_no]
    vicon_difference_df['LSHO-LUPA_y'] = vicon.iloc[:, LSHO_index_no+1] - vicon.iloc[:, LUPA_index_no+1]
    
    #vicon_difference_df['LSHO-LASI_x'] = vicon.iloc[:, LSHO_index_no] - vicon.iloc[:, LASI_index_no]
    #vicon_difference_df['LSHO-LASI_y'] = vicon.iloc[:, LSHO_index_no+1] - vicon.iloc[:, LASI_index_no+1]
    
    vicon_difference_df['LASI-RASI_x'] = vicon.iloc[:, LASI_index_no] - vicon.iloc[:, RASI_index_no]
    vicon_difference_df['LASI-RASI_y'] = vicon.iloc[:, LASI_index_no+1] - vicon.iloc[:, RASI_index_no+1]
    
    vicon_difference_df['RASI-RKNE_x'] = vicon.iloc[:, RASI_index_no] - vicon.iloc[:, RKNE_index_no]
    vicon_difference_df['RASI-RKNE_y'] = vicon.iloc[:, RASI_index_no+1] - vicon.iloc[:, RKNE_index_no+1]
    
    vicon_difference_df['RKNE-RANK_x'] = vicon.iloc[:, RKNE_index_no] - vicon.iloc[:, RANK_index_no]
    vicon_difference_df['RKNE-RANK_y'] = vicon.iloc[:, RKNE_index_no+1] - vicon.iloc[:, RANK_index_no+1]
    
    vicon_difference_df['RHEE-RANK_x'] = vicon.iloc[:, RHEE_index_no] - vicon.iloc[:, RANK_index_no]
    vicon_difference_df['RHEE-RANK_y'] = vicon.iloc[:, RHEE_index_no+1] - vicon.iloc[:, RANK_index_no+1]
    
    vicon_difference_df['LHEE-LANK_x'] = vicon.iloc[:, LHEE_index_no] - vicon.iloc[:, LANK_index_no]
    vicon_difference_df['LHEE-LANK_y'] = vicon.iloc[:, LHEE_index_no+1] - vicon.iloc[:, LANK_index_no+1]
    
    vicon_difference_df['LKNE-LANK_x'] = vicon.iloc[:, LKNE_index_no] - vicon.iloc[:, LANK_index_no]
    vicon_difference_df['LKNE-LANK_y'] = vicon.iloc[:, LKNE_index_no+1] - vicon.iloc[:, LANK_index_no+1]
    
    vicon_difference_df['LASI-LKNE_x'] = vicon.iloc[:, LASI_index_no] - vicon.iloc[:, LKNE_index_no]
    vicon_difference_df['LASI-LKNE_y'] = vicon.iloc[:, LASI_index_no+1] - vicon.iloc[:, LKNE_index_no+1]
    
    vicon_difference_df['LELB-LUPA_x'] = vicon.iloc[:, LELB_index_no] - vicon.iloc[:, LUPA_index_no]
    vicon_difference_df['LELB-LUPA_y'] = vicon.iloc[:, LELB_index_no+1] - vicon.iloc[:, LUPA_index_no+1]
    
    vicon_difference_df['RELB-RUPA_x'] = vicon.iloc[:, RELB_index_no] - vicon.iloc[:, RUPA_index_no]
    vicon_difference_df['RELB-RUPA_y'] = vicon.iloc[:, RELB_index_no+1] - vicon.iloc[:, RUPA_index_no+1]
    
    vicon_difference_df['LSHO-RSHO_x'] = vicon.iloc[:, LSHO_index_no] - vicon.iloc[:, RSHO_index_no]
    vicon_difference_df['LSHO-RSHO_y'] = vicon.iloc[:, LSHO_index_no+1] - vicon.iloc[:, RSHO_index_no+1]
    
    #print(vicon_difference_df.head());
    #print(vicon_difference_df.size);
    #print(vicon_difference_df.tail(3));
    return vicon_difference_df;

def read_jason_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data;

#json_data = read_jason_file(file_path);

def collect_person_keypoints(json_data):
    people = json_data['people'];
    key_points = people[0]['pose_keypoints_2d']# first person key_points
    
    return key_points;

#key_points = collect_person_keypoints(json_data);

def get_coordinates_list(list_of_keypoints, number_of_keypoints):
    if len(list_of_keypoints) != 75:
        print("ERROR: Number of elements in the list or not 25");
        return;
    
    list_of_coordinates = [];
    for i in range(number_of_keypoints):
        x = list_of_keypoints[i*3];
        y = list_of_keypoints[i*3 + 1];
        
        list_of_coordinates.append((x, y));
        
    return list_of_coordinates;    
        

def get_absolute_distance(key_points_coordinates, segments_list):
    segment_distance_points = [];
    for (a, b) in segments_list:
        (kxa,kya) = key_points_coordinates[a];
        (kxb,kyb) = key_points_coordinates[b];
        seg_dist_x = float(format((kxb - kxa) , ".3f"));
        seg_dist_y = float(format((kyb - kya), ".3f"));
        segment_distance_points.append((seg_dist_x, seg_dist_y));
    return segment_distance_points;
    



def extract_segments_openpose(file_path, segments_list):
    json_data = read_jason_file(file_path);
    key_points = collect_person_keypoints(json_data);
    key_points_coordinates = get_coordinates_list(key_points, number_of_keypoints);
    #print(key_points_coordinates);
    segment_distance_points_list = get_absolute_distance(key_points_coordinates, segments_list);

    #print("Segments differences calculated as : \n\n");
    #print(segment_distance_points_list);
    return segment_distance_points_list;
    
#extract_segments_openpose(file_path, segments_list);

vicon_segment_diff_dataframe = read_csv(vicon_file_path);
print(vicon_segment_diff_dataframe.head().to_string())


def dot_product(v1, v2):
    return sum(map(operator.mul, v1, v2))

def vector_cos(v1, v2):
    prod = dot_product(v1, v2)
    len1 = math.sqrt(dot_product(v1, v1))
    len2 = math.sqrt(dot_product(v2, v2))
    return prod / (len1 * len2)
    
def calculate_CS(openpose_kp_folder, vicon_segment_diff_dataframe):
    
    op_kp_files = os.listdir(openpose_kp_folder);
    all_rows_cs_res = [];
    kp_row_count = 0;
    vicon_segment_diff_dataframe_index = 0;
    for kp_file in op_kp_files:
        cur_row_res_list = [];
        file_path = os.path.join(openpose_kp_folder, kp_file);
        segment_distance_points_list = extract_segments_openpose(file_path, segments_list);
        print(segment_distance_points_list);
        #print('\n\n');
        #print(len(segment_distance_points_list));
        vicon_segment_diff_dataframe_index = kp_row_count * 4;
        vicon_segments_diff_df_col_index = 0;
        for i in range(len(segment_distance_points_list)):
            vector_OP = segment_distance_points_list[i];
            vicon_segments_diff_df_col_index = i*2;
            vector_vicon = (vicon_segment_diff_dataframe.iloc[vicon_segment_diff_dataframe_index][vicon_segments_diff_df_col_index], vicon_segment_diff_dataframe.iloc[vicon_segment_diff_dataframe_index][vicon_segments_diff_df_col_index+1])
            print(vector_OP)
            print(vector_vicon)
            cosin_sim = vector_cos(vector_OP, vector_vicon);
            #print(cosin_sim);
            cur_row_res_list.append(cosin_sim);
            #break;
        avg_CS_cur_row = sum(cur_row_res_list)/len(cur_row_res_list);
        cur_row_res_list.append(avg_CS_cur_row)
        print(cur_row_res_list)
        all_rows_cs_res.append(cur_row_res_list);
        kp_row_count += 1;
        break;
    return all_rows_cs_res;
        
calculate_CS(openpose_kp_folder, vicon_segment_diff_dataframe);