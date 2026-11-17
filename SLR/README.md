# Đầu ra cá nhân của tổng quan tài liệu

Tiến độ chung: [Week 6–7 tracker](../team-synthesis/week6-week7-tracker.md).

Mỗi thành viên dùng một mã ổn định, ví dụ `member-01`. Chỉ tạo thư mục khi đã phân công; hiện chưa có thành viên hoặc nguồn search được gán. Không lưu MSSV/email nếu không cần cho nghiên cứu.

```text
SLR/<member-id>/
  search-log.md
  01_all_records.csv
  02_after_screening_v1.csv
  03_final_included.csv
  prisma-flow.md
  evidence-table.md
  crosscheck.md
  rq-check.md
```

Tổng hợp nhóm lưu ở `team-synthesis/`; không duy trì nhiều bản tổng hợp khác nhau mà không ghi version. Những tệp trong cây trên là đầu ra dự kiến, chưa phải kết quả đã tạo.

## Quy tắc dữ liệu

- `record_id` ổn định từ tìm kiếm tới evidence; lưu nguồn, query và ngày. Snowballing có hướng và seed.
- Giữ dấu vết dedup và lý do nhận/loại; thiếu abstract cần xử lý theo protocol, không tự loại vì trống.
- Kết quả số và hạn chế phải dẫn trang/bảng/đoạn, ghi N/A khi không tìm thấy; không tự ước điền.
- Ghi người trích và người kiểm chéo, bất đồng và cách phân xử. Kiểm screening khác kiểm extraction.
- Preprint có thể bị loại khỏi tập tổng hợp theo tiêu chí nhưng vẫn cần xét nếu phản chứng novelty.
- Không commit API keys, token, dữ liệu cá nhân hoặc PDF/tài liệu chưa rõ quyền phân phối. Nguồn riêng tư ghi trong [source register](../team-synthesis/source-register.md).
- AI hỗ trợ gợi ý/trích nháp phải được khai báo và người nghiên cứu đối chiếu nguồn. Không đánh dấu có kiểm chéo bởi hai người khi chưa có hai người thực hiện.

Bắt đầu tìm chính thức sau khi `team-synthesis/review-protocol.md` và `team-synthesis/ie_criteria.md` được thống nhất. Chưa tạo số paper, số PRISMA hay nhãn novelty từ danh sách tham khảo sẵn có.
