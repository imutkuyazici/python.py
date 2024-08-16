def draw_simple_spiral(n):
    # Başlangıç noktaları
    x, y = 0, 0
    dx, dy = 0, 1  # İlk yön: sağa
    
    # Matris oluştur
    matrix = [[" " for _ in range(n)] for _ in range(n)]
    
    for _ in range(n * n):
        matrix[x][y] = "*"  # Yıldızı yerleştir
        # Bir sonraki pozisyonu hesapla
        nx, ny = x + dx, y + dy
        # Yön değiştirme kontrolü
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == " ":
            x, y = nx, ny
        else:
            dx, dy = dy, -dx  # Yönü değiştir
            x, y = x + dx, y + dy
    
    for row in matrix:
        print(" ".join(row))

# Spiral boyutu
n = 9
draw_simple_spiral(n)
