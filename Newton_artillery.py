import math
import matplotlib.pyplot as plt

def run_simulation():
    # ============================
    # 1. 参数设置 (您可以修改这里)
    # ============================
    m = 10.0          # 炮弹质量 (kg)
    v0 = 100.0        # 初速度 (m/s)
    angle_deg = 45.0  # 发射角度 (度)
    k = 0.02          # 空气阻力系数 (简化版: F = k * v^2)
    dt = 0.01         # 时间步长 (秒)，越小越精确
    g = 9.81          # 重力加速度 (m/s^2)

    # 初始速度分量
    angle_rad = math.radians(angle_deg)
    vx0 = v0 * math.cos(angle_rad)
    vy0 = v0 * math.sin(angle_rad)

    # ============================
    # 2. 伽利略模型 (理想抛物线)
    # ============================
    # 直接使用物理公式计算: x = v0*t, y = v0*t - 0.5*g*t^2
    galileo_x = []
    galileo_y = []
    
    t = 0
    while True:
        x = vx0 * t
        y = vy0 * t - 0.5 * g * t**2
        
        if y < 0: break # 落地停止
        
        galileo_x.append(x)
        galileo_y.append(y)
        t += dt

    # ============================
    # 3. 牛顿模型 (空气阻力, 数值积分)
    # ============================
    newton_x = [0]
    newton_y = [0]
    
    # 当前状态变量
    x, y = 0.0, 0.0
    vx, vy = vx0, vy0
    
    while y >= 0:
        # A. 计算当前瞬时总速度
        v = math.sqrt(vx**2 + vy**2)
        
        # B. 计算空气阻力 (F = k * v^2)
        f_drag = k * (v**2)
        
        # C. 将阻力分解到 X 和 Y 方向
        # 阻力方向永远与速度方向相反 (cos_theta = vx/v, sin_theta = vy/v)
        if v == 0: v = 0.0001 # 防止除以零
        f_drag_x = f_drag * (vx / v)
        f_drag_y = f_drag * (vy / v)
        
        # D. 计算加速度 (牛顿第二定律 a = F/m)
        ax = -(f_drag_x) / m
        ay = -g - (f_drag_y / m)
        
        # E. 更新速度和位置 (欧拉法)
        x  += vx * dt
        y  += vy * dt
        vx += ax * dt
        vy += ay * dt
        
        if y >= 0:
            newton_x.append(x)
            newton_y.append(y)

    # ============================
    # 4. 绘图与结果输出
    # ============================
    plt.figure(figsize=(10, 6))
    
    # 绘制曲线
    plt.plot(galileo_x, galileo_y, label='Galileo Model (Vacuum)', linestyle='--', color='gray')
    plt.plot(newton_x, newton_y, label='Newton Model (Air Drag)', color='red', linewidth=2)
    
    # 标注落地距离
    print(f"【模拟结果对比】")
    print(f"伽利略模型射程: {galileo_x[-1]:.2f} 米")
    print(f"牛顿模型射程:   {newton_x[-1]:.2f} 米")
    print(f"射程损失:       {100 - (newton_x[-1]/galileo_x[-1]*100):.1f}%")

    # 图表美化
    plt.title(f'Ballistic Trajectory Comparison\n(v0={v0}m/s, Mass={m}kg, Drag_k={k})')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.axhline(0, color='black', linewidth=1) # 地面线
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.axis('equal') # 保证 X 和 Y 轴比例一致，能看出真实形状
    
    plt.show()

if __name__ == "__main__":
    run_simulation()