# Gửi mail hoàng loạt bằng Python với nội dung và tệp đính kèm khác nhau

# 1. Chỉnh quyền GM
Vô gmail -> Quản lý tài khoản google -> Bảo mật -> Bật quyền truy cập cho ứng dụng kém an toàn lên 
![image](https://user-images.githubusercontent.com/76168991/138074844-47403b92-2adc-4f45-b985-57858eb3cfa1.png)

# 2. Chuẩn bị file excel
Đối với một số loại mail chỉ thay đổi cách xưng hô và đính kèm tệp khác nhau, ta cần tạo file excel để dễ dàng làm được việc này. 
![image](https://user-images.githubusercontent.com/76168991/138076245-a42fbcc5-a43a-4eb5-aac6-eb2bded6bac1.png)

Ở đây ví dụ tôi muốn gửi mail đến 2 người. Thay đổi cách xưng là Mr. Luật và Mrs. Trần. Bạn cũng có thể thêm nhiều cột khác, vd như giờ giấc hẹn, địa điểm khác nhau, ...<br>
Cần một cột "mail" để lưu mail của 2 người đó <br>
Cột "attachment_name" là tên của tệp đính kèm mà người đó sẽ nhận <br>
Cột "attachment_path" là đường dẫn tuyệt đối đến file đó. <br>

 Chú ý: sử dụng tên cột không có dấu, không cách 

# 3.Chuẩn bị template mail
Ở bước này, tạo 1 file template.txt để chứa mẫu email chung. Nhằm mục đích mail có nhiều định dạng khác nhau, nội dung mail phải được viết bằng HTML. Nếu bạn không biết HTML thì cũng đừng lo lắng, truy cập vào đường link sau https://wordhtml.com/ để tiến hành. <br> <br> 

![image](https://user-images.githubusercontent.com/76168991/138078071-2e9321cd-b992-4a64-9aa3-c3ebb06dab4c.png)
Ở đây biên soạn nội dung mail của bạn, những chỗ {} là nơi cần thêm giá trị từ các cột trong excel của mình 
![image](https://user-images.githubusercontent.com/76168991/138078497-d6ec4200-64ff-4f37-a359-7b3e29fe51cf.png) <br>
Ở file main.py dòng thứ 15, bỏ tên của các cột vào. Ghi như vậy tức nghĩa là giá trị của cột "mr" sẽ vào {} thứ 1, "name" sẽ vào {} thứ 2 <br>

Bây giờ chỉ cần bấm qua tab HTML, copy html ở đó và patse vào file template.txt
![image](https://user-images.githubusercontent.com/76168991/138078723-4ef182d2-dd19-4c9c-82f1-b6beb5f87c39.png)
![image](https://user-images.githubusercontent.com/76168991/138078752-c4628342-5ad6-4bd7-b2a4-e103a60eba62.png)

