% Post Lab Questions 
% Q1) 1.	Let x(n) = 8(0.5)n (u[n+1] - u[n-3]). 
% Sketch the following signals
% I.	Y(n) = [x-3]
% II.	F(n) = x[n+1]
% III.	G(n) = x[-n+4]


% Define the original signal x(n)
n = -5:10;
x_n = 8 * (0.5).^n .* (heaviside(n+1) - heaviside(n-3));

% I. Y(n) = [x-3]
Y_n = circshift(x_n, [0, -3]);

% II. F(n) = x[n+1]
F_n = circshift(x_n, [0, 1]);

% III. G(n) = x[-n+4]
G_n = circshift(flip(x_n), [0, -4]);

% Plotting the signals
figure;

subplot(4, 1, 1);
stem(n, x_n, 'b', 'LineWidth', 1.5);
title('x(n)');
xlabel('n');
ylabel('x(n)');

subplot(4, 1, 2);
stem(n, Y_n, 'r', 'LineWidth', 1.5);
title('Y(n) = [x-3]');
xlabel('n');
ylabel('Y(n)');

subplot(4, 1, 3);
stem(n, F_n, 'g', 'LineWidth', 1.5);
title('F(n) = x[n+1]');
xlabel('n');
ylabel('F(n)');

subplot(4, 1, 4);
stem(n, G_n, 'm', 'LineWidth', 1.5);
title('G(n) = x[-n+4]');
xlabel('n');
ylabel('G(n)');

sgtitle('Signal Sketches');

% Adjusting the plot layout
set(gcf, 'Position', get(0, 'Screensize')); % Maximize the figure window
