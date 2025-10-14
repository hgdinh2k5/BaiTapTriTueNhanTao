Báo cáo đồ án cá nhân trí tuệ nhân tạo
Đề tài: Giải bài toán đặt 8 quân xe lên bàn cờ với điều kiện chúng không ăn lẫn nhau bằng các thuật toán tìm kiếm
Giảng viên hướng dẫn: Phan Thị Huyền Trang 
Sinh viên thực hiện: Huỳnh Gia Định
Mã sinh viên: 23110092
1. Mục Tiêu
Mục tiêu của đề tài:
- Sử dụng các thuật toán tìm kiếm để tìm ra trạng thái các quân xe không ăn nhau trùng với trạng thái đích cho trước
- Thể hiện trực quan lên giao diện để người dùng hiểu đc cách hoạt động
2. Nội dung thực hiện

  2.1. Mô tả bài toán
  - Trạng thái ban đầu (Initial State): Bàn cờ 8x8 rỗng, gồm 64 ô được đánh số theo hàng và cột.
  - Trạng thái mục tiêu (Goal State): 8 quân xe được đặt trên bàn sao cho không quân nào đứng cùng hàng hoặc cùng cột – đảm bảo điều kiện “không ăn nhau”.
  - Tập hành động (Actions): Lần lượt đặt từng quân xe lên bàn theo quy tắc xác định vị trí hợp lệ.
  - Không gian trạng thái (State Space): Tất cả các trạng thái có thể sinh ra trong quá trình đặt quân.
  - Lời giải (Solution): Một ma trận 8x8 biểu diễn vị trí của 8 quân xe thỏa mãn điều kiện bài toán.

  2.2. Nhóm thuật toán tìm kiếm không có thông tin (Uninformed Search):

  Nhóm này bao gồm các thuật toán không sử dụng thông tin bổ sung về trạng thái đích mà chỉ dựa trên cấu trúc tìm kiếm. Các thuật toán được cài đặt gồm:
DFS, BFS, UCS, DLS, IDS.
    
    2.2.1. DFS(Depth-First Search):
  
![DFS](https://github.com/user-attachments/assets/d0c536f7-46eb-4ec5-af9a-f3f52590ea08)


    Sử dụng ngăn xếp (Stack) để lưu trữ các trạng thái, thuật toán sẽ mở rộng nhánh sâu nhất trước khi quay lại.
    Ưu điểm: Tiết kiệm bộ nhớ, có thể tìm lời giải nhanh nếu đích ở độ sâu nhỏ.
    Nhược điểm: Dễ rơi vào vòng lặp vô hạn.

    
  
    2.2.2. BFS (Breadth-First Search):
![BFS](https://github.com/user-attachments/assets/ebfc8b3a-0280-4229-841c-b7c53b714764)

  
    Dựa trên hàng đợi (Queue), BFS mở rộng tất cả các nút ở cùng một mức trước khi sang mức kế tiếp.
    Ưu điểm: Đảm bảo tìm được lời giải nếu có, và lời giải là ngắn nhất.
    Nhược điểm: Tiêu tốn bộ nhớ lớn do phải lưu tất cả các nút trong cùng một tầng.

    2.2.3. UCS (Uniform Cost Search):


![UCS_moi](https://github.com/user-attachments/assets/8f97e883-3df1-498e-a660-4c9dc2bcf300)



    Sử dụng hàng đợi ưu tiên (Priority Queue) để chọn nút có chi phí thấp nhất để mở rộng.
    Ưu điểm: Đảm bảo tìm được đường đi có tổng chi phí nhỏ nhất.
    Nhược điểm: Thời gian và bộ nhớ tiêu tốn lớn nếu có nhiều trạng thái có chi phí tương đương.
  
    2.2.4. DLS (Depth Limit Search)
    
  ![DLS](https://github.com/user-attachments/assets/bf60ad5d-d0bf-4020-a725-952ab33c3af3)

    Sử dụng thuật toán DFS để tìm kiếm nhưng có giới hạn độ sâu
    Ưu điểm: Tránh được vòng lặp vô hạn của DFS, giảm bớt không gian tìm kiếm.
    Nhược điểm: Không hoàn chỉnh nếu giới hạn nhỏ hơn độ sâu lời giải.
  
    2.2.5. IDS(Iterative Deepening Search)
  ![IDS](https://github.com/user-attachments/assets/ffc62d71-bb9e-4b8b-b6b3-570c94b05521)

    Kết hợp ưu điểm của DFS và BFS, thuật toán lặp lại quá trình DLS với giới hạn độ sâu tăng dần (limit = 0, 1, 2, …).
    Ưu điểm: Tiết kiệm bộ nhớ như DFS nhưng đảm bảo tìm thấy lời giải.
    Nhược điểm: Tốn thời gian do phải lặp lại nhiều cấp độ.
  
    2.2.6 So sánh hiệu suất
    - Biểu đồ thời gian thực thi
    
<img width="1033" height="627" alt="Screenshot 2025-10-14 165018" src="https://github.com/user-attachments/assets/5142d2ec-a82a-4628-b97b-96832a377b3a" />

    - Biểu đò số bước tìm kiếm

<img width="1038" height="640" alt="Screenshot 2025-10-14 165145" src="https://github.com/user-attachments/assets/4353e2f5-ed2e-4513-be2f-ba24e1e97433" />

    
    
    - Biểu đồ tổng hợp hiệu quả: 1/(Step x Time)
 <img width="1038" height="667" alt="Screenshot 2025-10-14 165218" src="https://github.com/user-attachments/assets/b01780f4-1a78-4e6c-88a3-0ee9fce3e054" />

  2.3. Nhóm thuật toán tìm kiếm có thông tin
  
  Các thuật toán này sử dụng hàm heuristic để ước lượng khoảng cách hoặc chi phí từ trạng thái hiện tại đến trạng thái đích.
  
      2.3.1 Greedy Search
  
![Greedy](https://github.com/user-attachments/assets/33398b7f-e948-4557-b33a-128c9e5b90cc)

      Lựa chọn mở rộng trạng thái có giá trị heuristic tốt nhất.
      Ưu điểm: tìm được lời giải nhanh chóng
      Nhược điểm: hiệu suất thuật toán phụ thuộc nhiều vào các hàm tính toán chi phí
  
      2.3.2. A* Search
 
![Asao](https://github.com/user-attachments/assets/269a68a3-a9cb-4b69-aa8e-6713ab9f2fa5)

      Kết hợp chi phí thực tế g(n) và ước lượng h(n) theo công thức: f(n) = g(n) + h(n).
      Ưu điểm: Đảm bảo tính tối ưu và đầy đủ nếu h(n) là heuristic chấp nhận được.
      Nhược điểm: Tốn bộ nhớ và khó xác định hàm heuristic phù hợp.
  
      2.3.3 So sánh hiệu suất
  
    - Biểu đồ thời gian thực thi
    - Biểu đò số bước tìm kiếm
    - Biểu đồ tổng hợp hiệu quả: 1/(Step x Time)
      
  2.4 Nhóm thuật toán tìm kiếm cục bộ (Local Search)

  
  Tập trung tìm kiếm trong một không gian trạng thái cố định, chỉ di chuyển sang trạng thái lân cận tốt hơn.
  
      2.4.1. Hill Climbing
![HIllClimbing](https://github.com/user-attachments/assets/2f164bec-b01e-4972-82a9-96222b4047c5)


      Chọn trạng thái lân cận tốt nhất để tiến tới.
      Ưu điểm: Đơn giản, sử dụng ít bộ nhớ.
      Nhược điểm: Dễ dừng ở cực trị địa phương.
  
      2.4.2. Genetic Algorithm
  
![Genetic](https://github.com/user-attachments/assets/d8705df8-bd89-4a66-b663-f35ba28edcd5)

      Dựa trên các cơ chế chọn lọc – lai ghép – đột biến để tạo ra thế hệ trạng thái mới.
      Ưu điểm: Tìm kiếm hiệu quả trong không gian lớn.
      Nhược điểm: Thiết kế hàm thích nghi và các toán tử lai ghép phức tạp
  
      2.4.3. Simulated Annealing
  ![Simulate](https://github.com/user-attachments/assets/b688ff56-8f62-4353-8afa-1a5bcf412714)

      Lấy cảm hứng từ quá trình nung chảy kim loại và làm nguội dần, cho phép di chuyển đến trạng thái xấu hơn với xác suất giảm dần theo thời gian.
      Ưu điểm: Có thể thoát khỏi cực trị địa phương.
      Nhược điểm: Cần chọn hàm xác suất và tốc độ giảm nhiệt độ hợp lý.
  
      2.4.4 Beam Search
  ![Beam_Search_1](https://github.com/user-attachments/assets/56035728-55de-4afa-9848-5189abf4c915)

      Giữ lại K trạng thái tốt nhất ở mỗi mức thay vì toàn bộ như BFS.
      Ưu điểm: Giảm đáng kể bộ nhớ cần dùng.
      Nhược điểm: Có thể bỏ qua lời giải tối ưu.
  
      2.4.5. So sánh hiệu suất
  
      - Biểu đồ thời gian thực thi.
      - Biểu đồ số bước thực hiện.
      - Biểu đồ hiệu quả 1/(Step × Time).
  
  2.5. Nhóm thuật toán tìm kiếm trong môi trường phức tạp (Complex Search)

  Nhóm này xử lý các bài toán trong môi trường không chắc chắn hoặc quan sát một
  
      2.5.1 AND-OR Search
  ![Andorsearch](https://github.com/user-attachments/assets/8d83908e-4508-47d4-9fea-e57a18bc9f4e)

        Phân biệt giữa nút lựa chọn (OR) và nút bắt buộc (AND) trong quá trình tìm kiếm.
        Ưu điểm: Mô phỏng tốt các bài toán có điều kiện phức tạp.
        Nhược điểm: Không thích hợp với không gian tìm kiếm lớn.
  
      2.5.2 Belief State Search

![SensorLess](https://github.com/user-attachments/assets/66f41e11-4da2-4fdf-b729-9daa256a8c57)

        Áp dụng khi không quan sát được trạng thái thật, chỉ biết tập hợp các khả năng có thể xảy ra.
        Ưu điểm: Giải quyết được bài toán trong môi trường không chắc chắn.
        Nhược điểm: Dễ bị rơi vào trạng thái suy luận sai hoặc cực trị địa phương.
  
      2.5.3. Partial Observation Search


![Partial_ob](https://github.com/user-attachments/assets/d07b75cb-8cfd-4dfe-adb7-0df2646ecadf)

        Tìm kiếm dựa trên thông tin quan sát được một phần.
        Ưu điểm: Kết hợp giữa tìm kiếm và suy luận.
        Nhược điểm: Khó xác định trạng thái chính xác, dễ lặp hoặc sai hướng.
  
      2.5.4. So sánh hiệu suất
  
      - Biểu đồ thời gian thực thi.
      - Biểu đồ số bước thực hiện.
      - Biểu đồ hiệu quả theo công thức 1 / (Step × Time).
  2.6. Nhóm thuật toán tìm kiếm dựa trên ràng buộc

Những thuật toán này tìm kiếm lời giải thỏa mãn các ràng buộc nhất định, chẳng hạn trong bài toán 8 quân xe là điều kiện không hai xe nào cùng hàng hoặc cùng cột.
  
      2.6.1. Backtracking Search
  
![Backtrack](https://github.com/user-attachments/assets/f8ad945f-ad14-4eee-9c3a-fdef581fd00c)

        Thực hiện tìm kiếm theo chiều sâu, quay lui khi gặp mâu thuẫn.
        Ưu điểm: Dễ hiểu, dễ triển khai, tiết kiệm bộ nhớ.
        Nhược điểm: Tốc độ chậm, không tận dụng được thông tin ràng buộc sớm.
  
      2.6.2. Forward Checking
  ![Forward](https://github.com/user-attachments/assets/41551a7e-726b-4ccc-8ff8-93d0ad5b5c91)


        Sau mỗi lần gán giá trị, loại bỏ trước các giá trị không hợp lệ cho các biến còn lại.
        Ưu điểm: Phát hiện xung đột sớm, giảm số lần quay lui.
        Nhược điểm: Tốn bộ nhớ hơn Backtracking.
  
      2.6.3. Constraint Propagation (AC-3)
      
 ![AC3](https://github.com/user-attachments/assets/fc6eda82-f0c7-4868-963e-6960926678c3)

        Liên tục loại bỏ các giá trị không hợp lệ trong miền giá trị (domain) cho đến khi các ràng buộc nhất quán.
        Ưu điểm: Loại trừ được nhiều giá trị sai, giảm số lần tìm kiếm lại.
        Nhược điểm: Tốn bộ nhớ và không giải quyết được mọi mâu thuẫn phức tạp.
  
      2.6.4. So sánh hiệu suất
  
        - Biểu đồ thời gian thực thi.
      - Biểu đồ số bước thực hiện.
      - Biểu đồ hiệu quả theo công thức 1 / (Step × Time).

      
      
      
      
