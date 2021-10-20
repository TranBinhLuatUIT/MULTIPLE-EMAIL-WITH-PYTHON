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

![image](https://user-images.githubusercontent.com/76168991/138078071-2e9321cd-b992-4a64-9aa3-c3ebb06dab4c.png) <br>
Ở đây biên soạn nội dung mail của bạn, những chỗ {} là nơi cần thêm giá trị từ các cột trong excel của mình 
![image](https://user-images.githubusercontent.com/76168991/138078497-d6ec4200-64ff-4f37-a359-7b3e29fe51cf.png) <br>
Ở file main.py dòng thứ 15, bỏ tên của các cột vào. Ghi như vậy tức nghĩa là giá trị của cột "mr" sẽ vào {} thứ 1, "name" sẽ vào {} thứ 2 <br>

Bây giờ chỉ cần bấm qua tab HTML, copy html ở đó và patse vào file template.txt
![image](https://user-images.githubusercontent.com/76168991/138078723-4ef182d2-dd19-4c9c-82f1-b6beb5f87c39.png)
![image](https://user-images.githubusercontent.com/76168991/138079730-af1098b4-d4b0-47bd-8956-f8fb3441a5ed.png)

# 4.Chỉnh tham số
Làm việc ở file main.py, một số biến cần lưu ý như: <br>
file_excel_path: đường dẫn đến file excel <br>
FROM: Tên của người gửi <br>
SUBJECT: Tiêu đề mail <br>
CONTENT_COL: list tên cột để điền vào những chỗ trống {} trong template <br>
TO_COL : tên của cột chứa địa chỉ mail trong file excel <br>
ATTACHMENT_PATH_COL: tên của cột chứa đường dẫn tệp đính kèm trong file excel. Nếu không cần gửi đường dẫn thì cứ để None<br>
ATTACHMENT_NAME_COL: tên của cột chứa tên tệp đính kèm muốn gửi <br>
![image](https://user-images.githubusercontent.com/76168991/138080086-475c0d9d-7ea8-4a57-89c7-6757334e031b.png)<br>
