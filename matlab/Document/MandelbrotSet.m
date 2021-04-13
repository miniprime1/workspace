[X, Y] = meshgrid(-2:0.01:1, -1:0.01:1);
C = X + 1i*Y;
Z = C;

for i = 1:400
    Z = Z.^2 + C;
end

hf = figure;
ha = axes(hf);
hp = pcolor(ha, X, Y, abs(Z));
shading(ha, 'interp')
xlabel('x')
ylabel('y')
colorbar();
colormap(flipud(colormap('hot')));