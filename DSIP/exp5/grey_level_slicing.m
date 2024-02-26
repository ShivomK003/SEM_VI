clearvars;
b = imread("kodak_pixpro_fz201_01.jpg");
b = rgb2gray(b);
z_nb = b;
z_b = b;
[r c] = size(b);
T1 = input("Enter value of threshold T1: ")
T2 = input("Enter value of threshold T2: ")
for i = 1:1:r
    for j = 1:1:c
        if((b(i, j) >=  T1) && (b(i, j) <= T2)) 
            z_nb(i, j) = 255;
            z_b(i, j) = 255;
        else
            z_nb(i, j) = 0;
            z_b(i, j) = 50;
        end
    end 
end
figure(1);
imshow(b);
figure(2);
imshow(z_nb);
figure(3);
imshow(z_b);