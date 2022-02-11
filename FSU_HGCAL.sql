use FSU_HGCAL;
drop table Full_Sensor;
create table Full_Sensor (  Sensor_ID varchar(32), Scratch_pad_ID varchar(32), Thick_ness varchar(32), P_Stop varchar(32), Oxide_type varchar(32), Flat_band_volt__V varchar(32), P_Stop_conc varchar(32), Proc varchar(32), Status_in_view_of_dicing_frame_removal varchar(32), Current_location varchar(32), RINSC_plan varchar(32), Pre_irrad_test_on_DF varchar(32), Pre_irrad_test_off_DF varchar(32), Sent_to_RINSC varchar(32), RINSC_irrad_round varchar(32), Post_irrad_test varchar(32) );
