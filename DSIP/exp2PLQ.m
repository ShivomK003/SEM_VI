% Post Lab Questions 
% Q1) 1.	Let x(n) = 8(0.5)n (u[n+1] - u[n-3]). 
% Sketch the following signals
% I.	Y(n) = [x-3]
% II.	F(n) = x[n+1]
% III.	G(n) = x[-n+4]



figure(1)

% given signal
subplot(2,2,1);
n = -5:10;
x_n = 8 * ((0.5) .^ n) .* ((n+1) >=0 & (n-3) < 0);
stem(n, x_n, 'r', 'LineWidth', 1.5);
title('Signal x(n)');

% Signal Y(n) = [x-3]
subplot(2,2,2);
shifted_n = n - 3;
shifted_x_n = zeros(size(n));
valid_indices = (shifted_n >= -5) & (shifted_n <= 10);
shifted_x_n(valid_indices) = x_n(shifted_n(valid_indices) + 5); % +5 to handle negative indices
stem(shifted_n(valid_indices), shifted_x_n(valid_indices), 'b', 'LineWidth', 1.5);

