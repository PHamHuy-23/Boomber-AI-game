# Bomberman AI - Handover Document

## 1. Tổng quan dự án

### Mục tiêu của dự án
Xây dựng một nền tảng Bomberman AI phục vụ:
- Chơi game trực tiếp trên web.
- Quan sát và so sánh nhiều agent AI cùng lúc.
- Trực quan hóa cách từng thuật toán ra quyết định.
- Phân tích kết quả nghiên cứu và chuẩn bị khung cho phần thực nghiệm/dataset.

### Phạm vi
Dự án hiện tại bao gồm:
- Game Bomberman chạy bằng FastAPI backend.
- Frontend dashboard web để điều khiển trận đấu và xem trực quan.
- Hệ thống agent AI đa dạng trong thư mục `agents/`.
- Hỗ trợ Fog of War ở phía backend và frontend.
- Khung trực quan hóa cây trạng thái, log hoạt động, và phần experiments placeholder.

Chưa bao gồm:
- Trace nội bộ đầy đủ và chính xác cho từng thuật toán.
- Dataset thực nghiệm hoàn chỉnh.
- Biểu đồ, dashboard phân tích thực nghiệm thật.

### Kiến trúc tổng thể
Kiến trúc đang đi theo mô hình tách lớp:
- `frontend/` xử lý hiển thị, điều khiển, trực quan hóa.
- `backend/app/` cung cấp API và điều phối game.
- `environment/` và `agents/` chứa logic môi trường và AI cũ/dự phòng.
- `backend/app/engine.py` là engine game đang được backend sử dụng trực tiếp.
- `database/` lưu SQLite và schema thống kê trận đấu.

### Công nghệ đang sử dụng
- Python 3.12
- FastAPI
- Pydantic
- SQLite3
- Vanilla HTML/CSS/JavaScript
- Web Audio API
- Pytest

## 2. Công việc đã hoàn thành

### Các module đã hoàn thành
- Backend API chính ở `backend/app/main.py`.
- Game engine ở `backend/app/engine.py`.
- Dashboard web mới ở `frontend/dashboard.html`.
- Logic tương tác frontend mới ở `frontend/dashboard.js`.
- Redirect từ `frontend/index.html` sang dashboard mới.

### Các tính năng đã có
- Start, Pause, Resume, Reset cho trận đấu.
- Điều chỉnh tốc độ mô phỏng.
- Chọn map preset.
- Chọn seed.
- Chọn số lượng agent.
- Chọn thuật toán cho từng player.
- Hỗ trợ `player_1` manual hoặc agent-controlled.
- God View / Agent View.
- Toggle Fog of War.
- Chọn agent focus cho chế độ quan sát.
- Khu board game có placeholder khi backend chưa sẵn sàng.
- Khu Algorithm Lab có whiteboard scaffold:
  - Zoom
  - Pan
  - Drag
  - Chọn node
  - Frontier / Closed / Reasoning panels
  - Log panel có search và filter
- Khu Experiments có khung kiến trúc chờ dataset.
- Backend trả `settings` cho frontend để đồng bộ trạng thái.
- Backend áp dụng Fog of War khi sinh state cho agent.

### Những quyết định thiết kế đã được chốt
- Dùng dashboard 3 khu vực thay cho slideshow cũ.
- Giữ một entry point đơn giản qua `frontend/index.html`.
- UI ưu tiên laptop và màn hình làm việc, không ưu tiên trình chiếu slide lớn.
- Frontend phải hiển thị game rõ ràng ngay cả khi backend chưa online.
- Phần experiments chỉ cần khung kiến trúc trước, chưa đổ dữ liệu thật.

### Các thay đổi quan trọng đã thực hiện
- Tách giao diện trình bày cũ ra khỏi trải nghiệm chính.
- Tạo dashboard hiện đại, responsive hơn.
- Mở rộng backend để nhận cấu hình:
  - `fog_of_war`
  - `fow_radius`
  - `map_preset`
  - `seed`
  - `agent_count`
  - `agent_configs`
- Thêm hỗ trợ map preset ở backend.
- Thêm scaffold trực quan hóa cây trạng thái.

## 3. Công việc đang thực hiện

### Hiện đang làm gì
Hiện tại dự án đang ở giai đoạn:
- Hoàn thiện lớp giao diện dashboard mới.
- Chuẩn bị nền tảng cho trực quan hóa thuật toán theo từng agent.
- Chuẩn bị cơ chế log và whiteboard để sau này gắn trace thật từ agent.

### Đã làm đến đâu
- UI và backend đã chạy được theo luồng mới.
- FOW đã được đưa vào luồng game cơ bản.
- Dashboard mới đã có 3 khu chính.
- Trace hiện tại mới là scaffold mô phỏng logic giải thích, chưa phải trace thật từ từng thuật toán.

### Những file hoặc module liên quan
- `frontend/dashboard.html`
- `frontend/dashboard.js`
- `frontend/index.html`
- `backend/app/main.py`
- `backend/app/engine.py`
- `agents/*.py`

### Những phần còn dang dở
- Trace thật cho từng thuật toán:
  - BFS
  - DFS
  - Greedy
  - A*
  - Hill Climbing
  - Simulated Annealing
  - And-Or Search
  - Online Search
  - Backtracking
  - Minimax
  - Expectimax
- Chưa có pipeline xuất dữ liệu trace chuẩn từ agent.
- Chưa có dataset thực nghiệm thật.
- Chưa có biểu đồ dashboard thực nghiệm thật.
- Chưa có model dữ liệu chuẩn hóa cho replay/trace.

## 4. Công việc còn lại

### Cao
1. Gắn trace thật cho agent.
   - Mục tiêu: ghi lại frontier, closed set, utility, alpha-beta, temperature, heuristic, reason.
   - Đầu vào: state game, thuật toán agent, bước mô phỏng.
   - Đầu ra mong muốn: log và tree dữ liệu thật cho từng thuật toán.

2. Chốt chế độ Fog of War chuẩn hơn.
   - Mục tiêu: đảm bảo Agent View phản ánh đúng phần agent biết và không biết.
   - Đầu vào: state backend, visibility rule, agent focus.
   - Đầu ra mong muốn: board và visualization nhất quán với thông tin quan sát.

3. Đồng bộ `player_1` manual/agent-controlled rõ ràng hơn.
   - Mục tiêu: tránh nhập nhằng giữa chế độ chơi tay và chế độ bot.
   - Đầu vào: UI selection, backend config.
   - Đầu ra mong muốn: điều khiển rõ ràng theo chế độ được chọn.

### Trung bình
1. Xây dựng dashboard experiments thật.
   - Mục tiêu: hiển thị so sánh thuật toán bằng biểu đồ.
   - Đầu vào: dataset, thống kê trận, kết quả benchmark.
   - Đầu ra mong muốn: biểu đồ win rate, latency, survival time, FOW impact.

2. Chuẩn hóa replay/trace format.
   - Mục tiêu: dễ lưu, tải, và phát lại trận đấu.
   - Đầu vào: state từng step, action từng agent, meta info.
   - Đầu ra mong muốn: JSON schema rõ ràng cho replay và analysis.

3. Làm sạch frontend tooltip, labels, and layout spacing.
   - Mục tiêu: tăng khả năng trình bày và đọc lâu dài.
   - Đầu vào: dashboard hiện tại.
   - Đầu ra mong muốn: UI gọn và thống nhất hơn.

### Thấp
1. Tối ưu animation và hiệu ứng thị giác.
   - Mục tiêu: tăng cảm giác trình diễn.
   - Đầu vào: CSS hiện tại.
   - Đầu ra mong muốn: animation mượt hơn nhưng không gây rối.

2. Mở rộng preset map.
   - Mục tiêu: có nhiều kịch bản chiến đấu hơn.
   - Đầu vào: map generator hoặc presets.
   - Đầu ra mong muốn: thêm map phục vụ demo và nghiên cứu.

3. Hoàn thiện tài liệu kỹ thuật trong README.
   - Mục tiêu: README khớp với kiến trúc hiện tại.
   - Đầu vào: trạng thái code mới.
   - Đầu ra mong muốn: hướng dẫn chạy và mô tả module chính xác hơn.

## 5. Các quyết định thiết kế (Design Decisions)

- Giữ kiến trúc tách biệt giữa frontend, backend, engine, agents.
- Frontend ưu tiên dashboard làm việc, không giữ slideshow cũ làm trung tâm.
- Không phá vỡ cấu trúc backend FastAPI hiện có.
- Dữ liệu game vẫn đi qua API HTTP để dễ debug và thay thế.
- Fog of War phải tồn tại ở cả game view và visualization view.
- Experiments được thiết kế dạng scaffold mở rộng, không hard-code vào layout cũ.

### Những quyết định KHÔNG được thay đổi
- Không đổi sang framework frontend lớn nếu chưa có yêu cầu rõ ràng.
- Không gộp toàn bộ logic agent vào frontend.
- Không bỏ API backend làm lớp trung gian.
- Không phá cấu trúc module agent hiện tại.

### Các nguyên tắc cần tuân thủ
- Giữ game board luôn dễ nhìn trên laptop.
- Không để UI tự co quá nhỏ hoặc quá lớn.
- Không trộn dữ liệu God View vào Agent View khi FOW bật.
- Mọi thay đổi lớn phải giữ tương thích với backend hiện có.

## 6. Kiến trúc hiện tại

### Frontend
- `frontend/dashboard.html`: layout dashboard mới.
- `frontend/dashboard.js`: điều khiển game, log, visualization, FOW.
- `frontend/index.html`: redirect sang dashboard mới.

### Backend
- `backend/app/main.py`: FastAPI routes, init/step, settings, FOW, agent config.
- `backend/app/engine.py`: game loop, movement, bombs, explosion, items.

### Game Engine
- Engine hiện tại đang dùng trong backend là `SimulationEngine`.
- Nó quản lý:
  - Grid
  - Agents
  - Bombs
  - Explosions
  - Game over logic

### AI Engine
- Các agent nằm trong `agents/`.
- Backend chọn agent bằng registry trong `backend/app/main.py`.
- Một số agent cần trace sâu hơn để trực quan hóa đúng bản chất.

### Visualization
- Board rendering ở frontend.
- Fog of War rendering theo agent focus.
- Whiteboard tree view là scaffold cho search visualization.
- Log panel là scaffold cho hoạt động của agent.

### Dataset
- Hiện chưa có dataset thực nghiệm thật.
- Chỉ có SQLite và thống kê trận đấu cơ bản.
- Khu experiments đã được chừa chỗ để cắm dataset sau.

### Quan hệ giữa các module
- Frontend gửi cấu hình trận đấu lên backend.
- Backend khởi tạo engine và agent instance.
- Engine trả state sau mỗi bước.
- Frontend render state và sinh log/visual scaffold.
- SQLite lưu thống kê trận khi game kết thúc.

## 7. Các quy ước của dự án

### Coding Convention
- Python rõ ràng, ưu tiên type hints khi sửa file backend.
- JavaScript dùng `const`/`let`, tránh biến global nếu có thể.
- Code mới nên chạy được trên môi trường hiện tại không cần thêm framework.

### Cấu trúc thư mục
- `backend/app/`: API và game loop.
- `agents/`: thuật toán AI.
- `environment/`: môi trường cũ/dự phòng và logic hỗ trợ.
- `frontend/`: toàn bộ giao diện web.
- `database/`: SQLite và schema.
- `benchmarks/`: benchmark, analysis, báo cáo.

### Quy tắc đặt tên
- Python module: snake_case.
- Agent class: PascalCase.
- Frontend DOM id: lowercase, rõ nghĩa, ưu tiên `kebab` hoặc `snake` tùy ngữ cảnh cũ.

### Style Guide
- UI phải ưu tiên rõ ràng, dễ quan sát, không quá rối.
- Mọi phần trực quan hóa phải đọc được trên laptop.
- Khi thêm tính năng mới, luôn giữ chế độ fallback hoặc placeholder.

## 8. Những vấn đề đã biết (Known Issues)

- Trace thuật toán hiện tại vẫn là scaffold, chưa phải log thật từ internal search state.
- `README.md` vẫn mô tả kiến trúc cũ và chưa cập nhật đầy đủ dashboard mới.
- `frontend/index.html` chỉ redirect sang dashboard mới, phần HTML cũ vẫn còn trong file và nên được dọn dẹp sau.
- Phần experiments chưa có dữ liệu thật.
- FOW trong backend hiện theo mô hình visibility đơn giản, chưa chắc đã là mô hình quan sát chính xác nhất cho mọi agent.
- Một số text encoding trong file cũ đang bị lỗi hiển thị, nhưng dashboard mới đã tránh dùng lại phần đó.

## 9. Các yêu cầu của người dùng

### Yêu cầu đã thống nhất
- Thiết kế lại toàn bộ website Bomberman AI theo hướng hiện đại, trực quan, phù hợp trình bày và nghiên cứu.
- Tối ưu giao diện cho laptop.
- Loại bỏ:
  - Đánh giá thực nghiệm phiên bản cũ
  - Đánh giá hiệu năng
  - Đối kháng thực tế
  - Sinh bản đồ
- Website chỉ còn 3 phần chính:
  - Chơi Game
  - Trực quan hóa thuật toán
  - Thực nghiệm
- Hỗ trợ nhiều agent cùng lúc.
- Cho phép chọn thuật toán riêng cho từng player.
- Có Start, Pause, Resume, Reset.
- Có điều chỉnh tốc độ mô phỏng.
- Có chọn map, seed, số agent.
- Có hỗ trợ Fog of War.
- God View và Agent View phải tách biệt rõ.
- Visualization phải phản ánh đúng phần agent biết và không biết.
- Phần log phải có search, filter, scroll, và theo từng agent.
- Phần cây trạng thái phải mở ra như whiteboard:
  - zoom
  - pan
  - kéo thả
  - click node
  - xem parent/children/heuristic/action
- Phần experiments hiện tại chỉ cần kiến trúc để sau này gắn dataset.

### Phiên bản mới nhất của yêu cầu
- Website không còn là slideshow trình bày cũ.
- Dashboard mới là giao diện chính.
- Handover này là phiên bản hiện tại của yêu cầu và trạng thái dự án.

## 10. Checklist

- ✅ Backend FastAPI chính đã có cấu hình trận đấu mới.
- ✅ Game engine chạy với seed và map preset.
- ✅ Frontend dashboard mới đã được tạo.
- ✅ Fog of War có mặt ở cả game view và agent view.
- ✅ Chọn thuật toán cho từng player đã có trong UI.
- ✅ Start / Pause / Resume / Reset đã có trong UI.
- ✅ Whiteboard scaffold cho cây trạng thái đã có.
- ✅ Log panel có filter và search đã có.
- ✅ Experiments section đã có khung kiến trúc.
- 🟨 Trace thuật toán thật cho từng agent.
- 🟨 Dashboard experiments thật với dataset.
- 🟨 README cập nhật theo kiến trúc mới.
- ⬜ Replay system chuẩn hóa.
- ⬜ Tối ưu/clean lại file cũ không còn cần thiết.

## 11. Hướng dẫn cho AI Agent tiếp theo

- Không được thay đổi các quyết định thiết kế đã chốt.
- Không tự ý đổi kiến trúc sang một hướng khác nếu chưa có yêu cầu rõ ràng.
- Chỉ tiếp tục các công việc còn dang dở ở mục 4 và 3.
- Nếu cần thay đổi lớn, phải giải thích rõ lý do, tác động, và phương án thay thế.
- Luôn giữ UI phù hợp laptop và tránh layout quá nặng.
- Khi xử lý visualization, ưu tiên tính giải thích và tính đúng hơn là hiệu ứng đẹp.
- Nếu có xung đột giữa God View và Agent View, phải ưu tiên nguyên tắc quan sát đúng thông tin mà agent thật sự có.
- Khi cần mở rộng trace, hãy instrument agent thật thay vì chỉ mô phỏng trên frontend.

