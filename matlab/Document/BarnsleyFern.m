N = 1000000;

xy = [0; 0];
fern = zeros(N, 2);

f_1 = [0 0; 0 0.16];
f_2 = [0.85 0.04; -0.04 0.85];
f_3 = [0.2 -0.26; 0.23 0.22];
f_4 = [-0.15 0.28; 0.26 0.24];

P = randsample(1:4, N, true, [0.01 0.85 0.07 0.07]);
for i = 2:N
    p = P(i - 1)
    if p == 1
        xy = f_1 * xy;
    elseif p == 2
        xy = f_2 * xy + [0; 1.6];
    elseif p == 3 
        xy = f_3 * xy + [0; 1.6];
    else
        xy = f_4 * xy + [0; 0.44];
    end
    
    fern(i, 1) = xy(1);
    fern(i, 2) = xy(2);
end
clearvars -except N fern % R2008a+

% Plotting the fern

%{
% Better detail, slower performance
c = linspace(0, 0.35, N - 1); c(end + 1) = 1;
colormap(summer(N));
set(gcf, 'Color', 'k', 'position', [10, 50, 800, 600]);
scatter(fern(:, 1), fern(:, 2), 0.1, c, 'o');
set(gca, 'Color', 'k');
%}

%
% Less detail, better performance
c = linspace(1, 0.2, N - 1); c(end + 1) = 0;
colormap(summer(N));
set(gcf, 'Color', 'k', 'position', [10, 50, 800, 600]);
scatter(fern(:, 1), fern(:, 2), 0.1, c, '.');
set(gca, 'Color', 'k');
%}