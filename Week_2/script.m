exit
# Octave 4.2.2, Sun Apr 29 20:37:06 2018 GMT <unknown@unknown>
exit
# Octave 4.2.2, Sun May 27 21:12:51 2018 GMT <unknown@unknown>
exit
# Octave 4.2.2, Mon May 28 21:22:28 2018 GMT <unknown@unknown>
exit
# Octave 4.2.2, Mon May 28 22:49:56 2018 GMT <unknown@unknown>
exit
# Octave 4.2.2, Mon Jun 04 09:39:29 2018 GMT <unknown@unknown>
A = [1 2 3; 4 5 6; 7 8 9]
exit
# Octave 4.2.2, Wed Jul 04 11:11:42 2018 GMT <unknown@unknown>
a = [1 2 3 4]
sum(a)
prod(a
)
A = [1 2 3; 4 5 6; 7 8 9]
B = [2 3 4; 5 6 7; 8 9 1]
A * B
A .* B
find(A < 3)
[r,c] = find(A < 3)
A
 
# Create magic matrices
# A matrix is called as magic matrix if sum of elements rowwise or
# columnwise is same
M = magic(4)
M = magic(5)
sum(A)
sum(a)
A = [1 2 3; 4 5 6; 7 8 9]
sum(A)
M = magic(4)
 
# To find maximum element column wise
max(M, [], 1)
 
# To find maximum element row wise
max(M, [], 2)
 
# To convert a matrix into vector
S = M(:)
max(S)
sum(M, 1)
sum(M, 2)
 
# Create identity matrix
I = eye(9)
 
# Flip up identity matrix, diagonal elements will swap
flipud(eye(9))
M = magic(4)
M = magic(4)
sum(A)
 
# Plotting curves ....
t = [0:0.01:0.98]
y1 = sin(2*pi*4*t)
plot(t, y1)
y2 = cos(2*pi*4*t)
plot(t, y2)

# Draw overlapping plots
hold on
plot(t, y2, 'r')
 
xlabel('time')
ylabel('value')
legend('ishan', 'dindorkar')

# Saving plot on local memory
cd 'C:\Machine_Learning\Week_2'; print -dpng 'myPlot.png'
close

# Open 2 plots simultanoulsy in 2 windows
figure(1); plot(t, y1);
figure(2); plot(t, y2);

# Create a subplot out of the current plot
subplot(1,2,1);
plot(t, y1);
subplot(1,2,2);

# Changing axes of plot
axis([0.5 1 -1 1])
A = magic(6)
A
imagesc(A)

# Fix range of colors
imagesc(A), colorbar, colormap gray


