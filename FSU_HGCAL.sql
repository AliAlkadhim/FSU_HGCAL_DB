use FSU_HGCAL;
drop table Full_Sensor;
create table Full_Sensor (  Sensor_ID varchar(32), Scratch_pad_ID varchar(32), Thick_ness varchar(32), P_Stop varchar(32), Oxide_type varchar(32), Flat_band_volt__V varchar(32), P_Stop_conc varchar(32), Proc varchar(32), Status_in_view_of_dicing_frame_removal varchar(32), Current_location varchar(32), RINSC_plan varchar(32), Pre_irrad_test_on_DF varchar(32), Pre_irrad_test_off_DF varchar(32), Sent_to_RINSC varchar(32), RINSC_irrad_round varchar(32), Post_irrad_test varchar(32) );
insert into Full_Sensor values ('N4791_1', '100088', '300', 'com', 'A', '-5', 'STD', 'FZ', 'removed from DF', 'CMU', null, 'Done, CERN', 'Done, CERN', 'CMU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_2', '100089', '300', 'com', 'A', '-5', 'STD', 'FZ', 'removed from DF', 'CMU', null, 'Done, CERN', 'Done, CERN', 'CMU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_3', '100090', '300', 'com', 'A', '-5', 'STD', 'FZ', 'off DF', 'CMU', null, null, null, 'CMU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_4', '100091', '300', 'com', 'A', '-5', 'STD', 'FZ', 'off DF', 'CMU', null, null, null, 'CMU Module Assembly', null, null );
insert into Full_Sensor values ('N4790_1', '100076', '300', 'com', 'B', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', 'sent, 29 Oct 21', '1', null );
insert into Full_Sensor values ('N4790_2', '100077', '300', 'com', 'B', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 2.0E15', 'Done, CERN', 'Done, CERN', 'sent, 29 Oct 21', '2', null );
insert into Full_Sensor values ('N4790_3', '100078', '300', 'com', 'B', '-2', 'STD', 'FZ', 'removed from DF', 'CERN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4790_4', '100079', '300', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'FSU', 'RINSC 2.0E15', null, null, null, 'TBD', null );
insert into Full_Sensor values ('N4790_5', '100080', '300', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'FSU', 'non-irr. ref', null, null, null, null, null );
insert into Full_Sensor values ('N4790_6', '100081', '300', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'NTU', null, null, null, 'NTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_6', '100093', '300', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', 'sent, 29 Oct 21', '1', null );
insert into Full_Sensor values ('N4791_7', '100094', '300', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 2.0E15', 'Done, CERN', 'Done, CERN', 'sent, 29 Oct 21', '2', null );
insert into Full_Sensor values ('N4791_8', '100095', '300', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'CERN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4791_9', '100096', '300', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'CERN', 'RINSC 2.0E15', 'Done, CERN', 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4791_10', '100097', '300', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'FSU', 'non-irr. ref', null, null, null, null, null );
insert into Full_Sensor values ('N4791_11', '100098', '300', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'FSU', null, null, null, null, null, null );
insert into Full_Sensor values ('N4791_12', '100099', '300', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'NTU', null, null, null, 'NTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_13', '100100', '300', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'NTU', null, null, null, 'NTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_18', '100105', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'TTU', null, '-', 'Done, CERN', 'TTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_19', '100106', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'TTU', null, '-', 'Done, CERN', 'TTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_20', '100107', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'IHEP', null, '-', 'Done, CERN', 'IHEP Module Assembly', null, null );
insert into Full_Sensor values ('N4791_21', '100108', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'IHEP', null, '-', 'Done, CERN', 'IHEP Module Assembly', null, null );
insert into Full_Sensor values ('N4791_22', '100109', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'TTU', null, null, null, 'TTU Module Assembly', null, null );
insert into Full_Sensor values ('N4791_23', '100110', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'IHEP', null, null, null, 'IHEP Module Assembly', null, null );
insert into Full_Sensor values ('N4791_24', '100111', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'IHEP', null, null, null, 'IHEP Module Assembly', null, null );
insert into Full_Sensor values ('N4791_25', '100112', '300', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'IHEP', null, null, null, 'IHEP Module Assembly', null, null );
insert into Full_Sensor values ('N4790_13', '100082', '300', 'com', 'D', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', 'sent 29 Oct 21', '1', null );
insert into Full_Sensor values ('N4790_14', '100083', '300', 'com', 'D', '-2', 'STD', 'FZ', 'removed from DF', 'BROWN', 'RINSC 2.0E15', 'Done, CERN', 'Done, CERN', 'sent 29 Oct 21', '2', null );
insert into Full_Sensor values ('N4790_15', '100084', '300', 'com', 'D', '-2', 'STD', 'FZ', 'removed from DF', 'CERN', 'RINSC 1.5E15', 'Done, CERN', 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4790_16', '100085', '300', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'FSU', 'RINSC 2.0E15', '-', 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4790_17', '100086', '300', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'FSU', 'non-irr. ref', null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4790_18', '100087', '300', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'FSU', null, null, null, null, null, null );
insert into Full_Sensor values (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_2', '200089', '200', 'com', 'A', '-5', 'STD', 'FZ', 'on DF', 'FSU', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_3', '200089(90?)', '200', 'com', 'A', '-5', 'STD', 'FZ', 'on DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_4', '200089(91?)', '200', 'com', 'A', '-5', 'STD', 'FZ', 'off DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4790_7', '200075', '200', 'com', 'B', '-2', 'STD', 'FZ', 'on DF', 'FSU --> BROWN', 'RINSC 4.0E15', null, 'Done, FSU', null, '3', null );
insert into Full_Sensor values ('N4790_8', '200076', '200', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'FSU --> BROWN', 'RINSC 5.5E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4790_9', '200077', '200', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'FSU --> BROWN', 'RINSC 4.0E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4790_10', '200078', '200', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'CERN', 'RINSC 5.5E15', null, 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4790_11', '200079', '200', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'CERN', 'non.irr. ref.', null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4790_12', '200080', '200', 'com', 'B', '-2', 'STD', 'FZ', 'off DF', 'CERn', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_6', '200092', '200', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'FSU --> BROWN', 'RINSC 4.0E15', null, 'Done, FSU', null, '3', null );
insert into Full_Sensor values ('N4792_7', '200093', '200', 'com', 'C', '-2', 'STD', 'FZ', 'removed from DF', 'FSU --> BROWN', 'RINSC 5.5E15', null, null, null, 'TBD', null );
insert into Full_Sensor values ('N4792_8', '200094', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'FSU --> BROWN', 'RINSC 4.0E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4792_9', '200095', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'FSU --> BROWN', 'RINSC 5.5E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4792_10', '200096', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', 'non.irr. ref.', null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_11', '200097', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_12', '200098', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_13', '200099', '200', 'com', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_18', '200104', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'on DF', 'FSU', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_19', '200105', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'on DF', 'FSU', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_20', '200106', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'on DF', 'FSU --> BROWN', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_21', '200107', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'on DF', 'FSU --> BROWN', null, null, null, null, null, null );
insert into Full_Sensor values ('N4792_22', '200108', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_23', '200109', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4792_24', '200110', '200', 'ind', 'C', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, null, null, null, null );
insert into Full_Sensor values ('N4790_19', '200081', '200', 'com', 'D', '-2', 'STD', 'FZ', 'on DF', 'FSU--> BROWN', 'RINSC 4.0E15', null, 'Done, FSU', null, '3', null );
insert into Full_Sensor values ('N4790_20', '200082', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'FSU--> BROWN', 'RINSC 5.5E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4790_21', '200083', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'FSU--> BROWN', 'RINSC 4.0E15', 'Done, FSU', 'TBD, FSU', null, 'TBD', null );
insert into Full_Sensor values ('N4790_22', '200084', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'CERN', 'RINSC 5.5E15', null, 'Done, CERN', null, 'TBD', null );
insert into Full_Sensor values ('N4790_23', '200085', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'CERN', 'non.irr. ref.', null, 'Done, CERN', null, null, null );
insert into Full_Sensor values ('N4790_24', '200086', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, null, null, null, null );
insert into Full_Sensor values ('N4790_25', '200087', '200', 'com', 'D', '-2', 'STD', 'FZ', 'off DF', 'CERN', null, null, null, null, null, null );
select * from Full_Sensor;
