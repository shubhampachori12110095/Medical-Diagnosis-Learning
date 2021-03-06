#!/bin/bash

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_2_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_2_top1_valid_data.pkl' | tee content2.profile

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_3_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_3_top1_valid_data.pkl' | tee content3.profile

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_4_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_4_top1_valid_data.pkl' | tee content4.profile

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_5_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_5_top1_valid_data.pkl' | tee content5.profile

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_1_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_1_top1_valid_data.pkl' | tee content1.profile

# ====================================================================================================
# stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_2_top1_nopunc_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_2_top1_nopunc_valid_data.pkl' | tee content2_nopunc.profile
#
# stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_3_top1_nopunc_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_3_top1_nopunc_valid_data.pkl' | tee content3_nopunc.profile
#
# stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_4_top1_nopunc_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_4_top1_nopunc_valid_data.pkl' | tee content4_nopunc.profile
#
# stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_5_top1_nopunc_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_5_top1_nopunc_valid_data.pkl' | tee content5_nopunc.profile
#
# stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_1_top1_nopunc_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/10codesL5_UNK_content_1_top1_nopunc_valid_data.pkl' | tee content1_nopunc.profile

# ====================================================================================================
#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top100_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top100_valid_data.pkl' | tee content4_100.profile
#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top5_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top5_valid_data.pkl' | tee content4_5.profile
#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top10_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top10_valid_data.pkl' | tee content4_10.profile

#stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top1_valid_data.pkl' | tee content4_1_2.profile

# ====================================================================================================

stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_2_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_2_top1_valid_data.pkl' | tee content2_50.profile
stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_3_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_3_top1_valid_data.pkl' | tee content3_50.profile
stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_4_top1_valid_data.pkl' | tee content4_50.profile
stdbuf -oL python ../profile_dataset.py --train_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_5_top1_train_data.pkl' --val_path '/misc/vlgscratch2/LecunGroup/laura/medical_notes/processed_data/50codesL5_UNK_content_5_top1_valid_data.pkl' | tee content5_50.profile
