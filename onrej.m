
close all
clear all
%%

Nsig=14;                   %number of eeg siganls
Fs=512;                   %sampeling frequency
EndTime=180;
Nsamp=EndTime*Fs;

times=1/Fs:1/Fs:EndTime;

fid=fopen('onrej1.fdt');
f_nums=fread(fid,Nsamp);

fid1=fopen('onrej2.fdt');
f_nums1=fread(fid1,Nsamp);

fid2=fopen('onrej3.fdt');
f_nums2=fread(fid2,Nsamp);

fid3=fopen('onrej4.fdt');
f_nums3=fread(fid3,Nsamp);


fid5=fopen('onrej5.fdt');
f_nums5=fread(fid5,Nsamp);

fid6=fopen('onrej6.fdt');
f_nums6=fread(fid6,Nsamp);

fid7=fopen('onrej7.fdt');
f_nums7=fread(fid7,Nsamp);


fid8=fopen('onrej8.fdt');
f_nums8=fread(fid8,Nsamp);

fid9=fopen('onrej9.fdt');
f_nums9=fread(fid9,Nsamp);

fid10=fopen('onrej10.fdt');
f_nums10=fread(fid10,Nsamp);

fid11=fopen('onrej11.fdt');
f_nums11=fread(fid11,Nsamp);

fid12=fopen('onrej12.fdt');
f_nums12=fread(fid12,Nsamp);

fid13=fopen('onrej13.fdt');
f_nums13=fread(fid13,Nsamp);

fid14=fopen('onrej14.fdt');
f_nums14=fread(fid14,Nsamp);
%{
f_nums=f_nums/max(f_nums);
f_nums1=f_nums1/max(f_nums1);
f_nums2=f_nums2/max(f_nums2);
f_nums3=f_nums3/max(f_nums3);
f_nums5=f_nums5/max(f_nums5);
f_nums6=f_nums6/max(f_nums6);
f_nums7=f_nums7/max(f_nums7);
f_nums8=f_nums8/max(f_nums8);
f_nums9=f_nums9/max(f_nums9);
f_nums10=f_nums10/max(f_nums10);
f_nums11=f_nums11/max(f_nums11);
f_nums12=f_nums12/max(f_nums12);
f_nums50=f_nums50/max(f_nums50);
f_nums14=f_nums14/max(f_nums14);

%}


F_nums=reshape(f_nums,1,[]);
F_nums1=reshape(f_nums1,1,[]);
F_nums2=reshape(f_nums2,1,[]);
F_nums3=reshape(f_nums3,1,[]);
F_nums5=reshape(f_nums5,1,[]);
F_nums6=reshape(f_nums6,1,[]);
F_nums7=reshape(f_nums7,1,[]);
F_nums8=reshape(f_nums8,1,[]);
F_nums9=reshape(f_nums9,1,[]);
F_nums10=reshape(f_nums10,1,[]);
F_nums11=reshape(f_nums11,1,[]);
F_nums12=reshape(f_nums12,1,[]);
F_nums13=reshape(f_nums13,1,[]);
F_nums14=reshape(f_nums14,1,[]);

F_nums=(1/6)*eegfilt(F_nums,Fs,50,150);
F_nums1=(1/6)*eegfilt(F_nums1,Fs,50,150);
F_nums2=(1/6)*eegfilt(F_nums2,Fs,50,150);
F_nums3=(1/6)*eegfilt(F_nums3,Fs,050,150);
F_nums5=(1/6)*eegfilt(F_nums5,Fs,050,150);
F_nums6=(1/6)*eegfilt(F_nums6,Fs,050,150);
F_nums7=(1/6)*eegfilt(F_nums7,Fs,050,150);
F_nums8=(1/6)*eegfilt(F_nums8,Fs,050,150);
F_nums9=(1/6)*eegfilt(F_nums9,Fs,050,150);
F_nums10=(1/6)*eegfilt(F_nums10,Fs,050,150);
F_nums11=(1/6)*eegfilt(F_nums11,Fs,050,150);
F_nums12=(1/6)*eegfilt(F_nums12,Fs,050,150);
F_nums13=(1/6)*eegfilt(F_nums13,Fs,050,150);
F_nums14=(1/6)*eegfilt(F_nums14,Fs,050,150);



D={F_nums,F_nums1,F_nums2,F_nums3,F_nums5,F_nums6,F_nums7,F_nums8,F_nums9,F_nums10,F_nums11,F_nums12,F_nums13,F_nums14};


save D.mat D;