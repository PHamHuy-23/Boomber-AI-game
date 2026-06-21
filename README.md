# BombermanAI

Một project mô phỏng game Bomberman phục vụ nghiên cứu và đánh giá các thuật toán Trí tuệ Nhân tạo (AI Agent). Dự án được viết bằng Python 3.12, tách biệt hoàn toàn giữa Environment (Môi trường game) và Agent (Trí tuệ nhân tạo).

---

## 1. Kiến Trúc Dự Án (Environment-Agent Architecture)

Dự án áp dụng triết lý thiết kế của các thư viện Reinforcement Learning (như OpenAI Gym), trong đó:
* **Environment (Môi trường)**: Quản lý toàn bộ vòng đời và trạng thái của trò chơi (bản đồ, vị trí người chơi, kẻ địch, bom, vụ nổ, vật phẩm nâng cấp, điểm số). Môi trường hoàn toàn độc lập và không phụ thuộc vào lớp tác nhân (Agent). Nó tiếp nhận hành động (`action`) từ Agent bên ngoài, cập nhật thế giới game theo các quy tắc vật lý và luật chơi, rồi trả về trạng thái mới (`next_state`), phần thưởng (`reward`), trạng thái kết thúc (`done`) và các thông tin bổ sung (`info`).
* **Agent (Tác nhân AI)**: Nhận đầu vào là biểu diễn trạng thái của môi trường (`state`) dưới dạng một dictionary và đưa ra quyết định hành động tiếp theo (`action`) mà không có bất kỳ quyền can thiệp trực tiếp nào vào dữ liệu nội bộ của môi trường.

```
                  +-----------------------+
                  |      Environment      |
                  |                       |
                  | - Map, Bombs, Items   |
                  | - Enemies & Physics   |
                  +-----------+-----------+
                              ^     |
            action (Decision) |     | state (Observation)
                              |     v
                  +-----------+-----------+
                  |         Agent         |
                  |                       |
                  | - Choose next action  |
                  | - Random / Heuristics |
                  +-----------------------+
```

---

## 2. Cấu Trúc Thư Mục (Folder Structure)

```text
BombermanAI/
├── configs/
│   └── default_config.py      # Cấu hình tham số trò chơi (kích thước, mật độ vật cản, thời gian đếm ngược...)
├── environment/
│   ├── __init__.py            # Expose các lớp chính của Environment
│   ├── env.py                 # Lớp Environment trung tâm điều phối game
│   ├── map.py                 # Khởi tạo bản đồ, tường, gạch và kiểm tra đường đi kết nối (reachability)
│   ├── player.py              # Trạng thái người chơi chính (vị trí, máu, số bom tối đa, bán kính nổ)
│   ├── enemy.py               # Trạng thái kẻ địch và thuật toán di chuyển ngẫu nhiên/heuristic cơ bản
│   ├── bomb.py                # Quản lý vòng đời và đếm ngược của bom
│   ├── explosion.py           # Tính toán phạm vi nổ, kích hoạt nổ dây chuyền (chain-reaction) và sát thương
│   └── item.py                # Định nghĩa các vật phẩm nâng cấp (tăng tầm nổ, tăng số lượng bom)
├── agents/
│   ├── __init__.py            # Định nghĩa Interface BaseAgent
│   ├── random_agent.py        # Tác nhân AI di chuyển ngẫu nhiên (RandomAgent)
│   ├── minimax_agent.py       # Placeholder cho thuật toán tìm kiếm Minimax (TODO)
│   └── expectimax_agent.py    # Placeholder cho thuật toán Expectimax (TODO)
├── benchmark/
│   ├── __init__.py            # Expose các hàm benchmark
│   └── benchmark.py           # Vòng lặp chạy game và đánh giá hiệu năng agent
├── metrics/
│   ├── __init__.py            # Expose lớp theo dõi số liệu
│   └── metrics.py             # Thu thập số liệu trận đấu (Win Rate, Score, Steps...)
├── main.py                    # Điểm chạy chương trình chạy benchmark thử nghiệm
├── requirements.txt           # Danh sách thư viện phụ thuộc (numpy, pandas)
├── .gitignore                 # Bỏ qua các file không cần thiết khi commit git
└── README.md                  # Tài liệu giới thiệu dự án
```

---

## 3. Biểu Diễn Trạng Thái & Hành Động (State & Action Space)

### Không Gian Hành Động (Action Space)
Agent có thể lựa chọn 1 trong 6 hành động sau ở mỗi bước (step):
* `UP`: Di chuyển lên trên 1 ô.
* `DOWN`: Di chuyển xuống dưới 1 ô.
* `LEFT`: Di chuyển sang trái 1 ô.
* `RIGHT`: Di chuyển sang phải 1 ô.
* `BOMB`: Đặt bom tại vị trí hiện tại (nếu còn bom khả dụng).
* `WAIT`: Đứng yên tại chỗ.

### Cấu Trúc Trạng Thái (State Representation)
Trạng thái được truyền vào hàm `choose_action(state)` là một Python `dict` bao gồm các thông tin:
```python
state = {
    "self_position": (x, y),                # Vị trí của Agent (tuple)
    "enemy_positions": [(x, y), ...],       # Vị trí của các kẻ địch còn sống (list of tuples)
    "bomb_positions": [(x, y, timer), ...], # Vị trí và thời gian đếm ngược của bom trên bản đồ (list of tuples)
    "explosions": [(x, y), ...],            # Các ô đang bị bao phủ bởi lửa nổ (list of tuples)
    "walls": [(x, y), ...],                 # Vị trí các bức tường cứng không thể phá hủy (list of tuples)
    "items": {(x, y): "ItemType", ...},     # Vị trí và loại vật phẩm nâng cấp trên bản đồ (dict)
    "ammo": 1,                              # Số bom Agent có thể đặt tại thời điểm hiện tại (int)
    "blast_radius": 2,                      # Bán kính nổ của bom đặt bởi Agent (int)
    "time_remaining": 300                   # Số bước đi (ticks) còn lại trước khi hết giờ (int)
}
```

---

## 4. Hướng Dẫn Cài Đặt và Chạy Benchmark

### Yêu cầu hệ thống
* Python 3.12

### Cài đặt thư viện phụ thuộc
Cài đặt các thư viện bắt buộc (như `numpy` và `pandas` dùng để thống kê hiệu năng):
```bash
pip install -r requirements.txt
```

### Chạy Benchmark
Để chạy thử nghiệm benchmark mặc định gồm 10 trận đấu sử dụng `RandomAgent`:
```bash
python main.py
```

Sau khi chạy xong, chương trình sẽ hiển thị báo cáo hiệu năng:
```text
=== BENCHMARK REPORT (10 Games) ===
Win Rate:              0.00%
Average Score:         10.00
Average Steps:         15.40
Average Survival Time: 15.40 ticks
============================================
```

---

## 5. Định Hướng Phát Triển Tiếp Theo (AI Research)
* Cài đặt thuật toán đối kháng **Minimax** trong `agents/minimax_agent.py` để tối ưu hóa quyết định trong môi trường deterministic.
* Cài đặt thuật toán đối kháng xác suất **Expectimax** trong `agents/expectimax_agent.py` nhằm đối phó với kẻ địch di chuyển ngẫu nhiên.
* Xây dựng mô hình Học sâu củng cố (Deep Reinforcement Learning - DRL) như DQN hay PPO tận dụng thông tin trạng thái mở rộng từ môi trường.
