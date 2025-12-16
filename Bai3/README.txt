Pokémon là những sinh vật ẩn chứa nhiều bí mật sinh sống xung quanh con người tại thành phố Goldenrod. Một số Pokémon sống cùng với con người cũng như một số khác sống trong tự nhiên trên những cánh đồng cỏ, hang động, hoặc biển cả. Pokémon có thể được mang theo bằng cách sử dụng 1 loại bóng chứa mang tên Poké ball. Mỗi người dân trong thành phố Goldenrod này hầu hết đều mang theo mình từ 3 Pokemon trở lên.

Là một người đam mê tin học cũng như Pokemon, lớp trưởng Satoshi của IT002.M23.MTCL đã lên kế hoạch viết một chương trình để giúp mọi người có thể thi đấu Pokemon với nhau. 

Chương trình ban đầu của Satoshi khá cơ bản với chỉ 4 hệ: Nước, Lửa, Đất và Cỏ. 
Quy tắc tương khắc hệ như sau:
- Nước khắc Hỏa (gây thêm 20% sát thương)
- Hỏa khắc Cỏ (gây thêm 25% sát thương)
- Cỏ khắc Đất (gây thêm 15% sát thương)
- Đất khắc Nước (gây thêm 30% sát thương)
- Cỏ khắc Nước (gây thêm 10% sát thương)
- Đất khắc Lửa (gây thêm 35% sát thương)

Những trường hợp khắc hệ này sẽ gây ra nhiều hơn % sát thương so với chỉ số cơ bản ban đầu (có đề cập ở trên).

[Quy tắc thi đấu]
1. Mỗi lượt sẽ là 1 con Pokemon ra chiêu thức gây sát thương. 
2. Pokemon yếu hơn sẽ được ra chiêu ở lượt đầu tiên. 
3. Để xác định kẻ mạnh/yếu: 2 Pokemon sẽ được so sánh trên 3 phương diện:
   - Máu (HP)
   - Sát thương (Attack)
   - Tương khắc hệ
   -> Pokemon nào vượt trội hơn từ 2 tiêu chí trở lên sẽ là Pokemon mạnh hơn. Satoshi đã sử dụng toán tử lớn hơn hoặc nhỏ hơn để thực hiện việc so sánh này.

Để có thể tham gia vào chương trình thi đấu của Satoshi, 1 Pokemon sẽ phải có đầy đủ thông tin về: Tên, Hệ, Máu và Sát thương gây ra.

[Yêu cầu]
Do 1 lần quên logout, chương trình của Satoshi đã bị mất cắp. Nhờ các bạn còn lại của lớp IT002.M23.MTCL phục hồi lại nguyên vẹn chương trình của Satoshi, thực hiện các yêu cầu sau:

a. Thực hiện nhập danh sách các Pokemon sử dụng Vector hoặc Pointer (các thông tin tên, máu, sát thương, hệ tự nhập vào bàn phím).

b. Xuất thông tin chi tiết các Pokemon ra màn hình.

c. Viết 1 phương thức cho 2 Pokemon trong danh sách thi đấu với nhau, với tham số truyền vào được quy định là danh sách pokemon đã được nhập ở trên và vị trí của pokemon đó trong danh sách (đánh số thứ tự từ 1).
   - Kết quả mỗi lượt đánh của Pokemon sẽ được ghi chi tiết ra console những thông tin về số máu còn lại của các pokemon.
   - Khi 1 pokemon bị hạ gục, hãy thông báo kết quả người chiến thắng ra 1 file text “WINNER.OUT” và kết thúc chương trình.
