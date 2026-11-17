# Theo dõi nghiên cứu Week 6–7

Ngày khởi tạo: 17/11/2026 (giờ Việt Nam).

Repo chính: https://github.com/quachtheduong0212-droid/kgqa-semantics-verifiable

## Trạng thái hiện tại

Đã có bài FISAT, nhận xét reviewer, tài liệu hướng dẫn W6/W7 và đề cương định hướng. Google Docs đã đọc trực tiếp ngày 17/11/2026; kiểm tra 76 đoạn dài cho thấy khớp nội dung snapshot trong repo sau chuẩn hóa định dạng. Việc này chưa xác nhận tài liệu tham khảo, novelty, chính sách journal hay tái lập kết quả.

Chưa có sản phẩm literature review có hệ thống trong repo. Chưa khóa RQ, dataset, metric, baseline, ngưỡng hoặc thiết kế thực nghiệm. Không có kết quả mới cho bản mở rộng.

- **Đã ghi nhận:** nguồn hoặc quyết định có căn cứ; không đồng nghĩa đạt yêu cầu nghiên cứu.
- **Chưa bắt đầu:** chưa có sản phẩm đủ để rà soát.
- **Đang làm:** có người nhận việc và bản nháp/bằng chứng đang được bổ sung.
- **Chờ rà soát:** sản phẩm đã có, chưa hoàn thành kiểm chéo hoặc xác nhận cần thiết.
- **Hoàn tất:** có sản phẩm, kiểm tra và bằng chứng đạt điều kiện trong bảng.
- **Bị chặn:** ghi prerequisite cụ thể, tác động và việc cần làm tiếp.

Chưa phân công người thực hiện/người kiểm chéo. Khi nhận việc, thêm tên hoặc mã thành viên, ngày và liên kết commit/file vào cột cuối. Các đường dẫn trong dấu mã dưới đây là vị trí dự kiến, không khẳng định file đã tồn tại.

## Chuẩn bị

| ID | Việc | Trạng thái | Đầu ra / điều kiện hoàn tất | Phụ trách · bằng chứng |
|---|---|---|---|---|
| PRE-01 | Ghi nhận tài liệu nguồn | Đã ghi nhận | [Danh mục nguồn](source-register.md); tách bài nền, review, hướng dẫn và đề cương | Tệp do tác giả cung cấp; Google Docs đã đọc; metadata tham khảo còn cần kiểm |
| PRE-02 | Xác định repo theo dõi chính | Đã ghi nhận | [D001](decision-log.md); không coi Docs hoặc chat là nơi duy nhất lưu quyết định | Người dùng chỉ định repo ngày 17/11/2026 |
| PRE-03 | Chốt RQ sơ bộ và phạm vi search | Chưa bắt đầu | `rq-scope.md`: câu hỏi sơ bộ, P/I/C/O, người hưởng lợi, ngôn ngữ/task/ontology, loại câu hỏi ngoài phạm vi | Chưa phân công; bốn RQ trong đề cương chỉ là đầu vào |
| PRE-04 | Kiểm khả thi ban đầu | Chưa bắt đầu | `notes.md`: dữ liệu tải/mở được, một mục chạy được, công cụ đo dùng được, nguồn lực và blocker | Không dùng synthetic smoke test của setup thay bằng chứng dữ liệu nghiên cứu |
| PRE-05 | Thống nhất cách áp dụng W6/W7 | Chưa bắt đầu | Ghi quyết định áp dụng cho học phần/journal, yêu cầu giảng viên nếu có, điều chỉnh và lý do | W6/W7 là khung; không mặc định mọi quy định môn là yêu cầu journal |

## Week 6 · RBL-1: xây nền bằng chứng

| ID | Việc theo hướng dẫn | Trạng thái | Vị trí đầu ra · điều kiện hoàn tất | Phụ trách · bằng chứng |
|---|---|---|---|---|
| W6-01 | Chia nguồn; viết protocol và IC/EC trước search chính thức | Chưa bắt đầu | `review-protocol.md`, `ie_criteria.md`: RQ sơ bộ, nguồn/người, trường/năm, query, tiêu chí, kiểm chéo, đánh giá chất lượng, cách tổng hợp, ngày dừng | Chưa phân công |
| W6-02 | Xây và thử search string | Chưa bắt đầu | `SLR/<member-id>/search-log.md`: string gốc và cú pháp theo nguồn, thử nghiệm, ngày, số kết quả, lý do đổi | Chưa phân công |
| W6-03 | Tìm và lưu record | Chưa bắt đầu | `SLR/<member-id>/01_all_records.csv`: record ID, nguồn, query/ngày, title/year/DOI/abstract, provenance; kiểm metadata | Chưa phân công |
| W6-04 | Dedup và screening vòng 1 | Chưa bắt đầu | `02_after_screening_v1.csv`: giữ ID, quyết định/IC-EC/reason; Unsure khi thiếu căn cứ; log số trước/sau | Chưa phân công |
| W6-05 | Lấy full-text và ghi phiên bản | Chưa bắt đầu | `search-log.md`: URL/DOI, phiên bản đã đọc, ngày, tình trạng truy cập; dùng vị trí lưu được phép chia sẻ | Chưa phân công |
| W6-06 | Screening vòng 2, ghi near_rq | Chưa bắt đầu | `03_final_included.csv`: quyết định/reason/P-I-C-O; preprint liên quan vẫn được kiểm như ứng viên phản chứng | Chưa phân công |
| W6-07 | Chọn seed, backward/forward snowballing | Chưa bắt đầu | `search-log.md`: lý do chọn seed, DOI, hướng, bộ lọc, số xem/thêm/include; record mới qua cùng screening | Chưa phân công |
| W6-08 | Chốt tập và PRISMA từng nguồn | Chưa bắt đầu | `SLR/<member-id>/prisma-flow.md`: tách search/snowball; tất cả số truy được về CSV | Chưa phân công |
| W6-09 | Trích xuất evidence | Chưa bắt đầu | `SLR/<member-id>/evidence-table.md`: paper, tool, dataset, metric, đối chứng, kết quả, code, hạn chế, near_rq, tin cậy; trích thử và dẫn trang/bảng | Chưa phân công |
| W6-10 | Kiểm chéo screening và extraction | Chưa bắt đầu | `SLR/<member-id>/crosscheck.md`: mẫu/seed, người kiểm độc lập, bất đồng và cách xử lý; hai loại kiểm không thay thế nhau | Chưa phân công |
| W6-11 | Gộp bằng chứng và PRISMA nhóm | Chưa bắt đầu | `evidence-table-merged.md`, `prisma-team.md`: dedup giữa nguồn/study versions; số khớp, limitations của review | Chưa phân công |
| W6-12 | Evidence map và phân công phản chứng | Chưa bắt đầu | `rq-evidence-map.md`: P/I/C/O có nguồn nào, thiếu gì; mọi ứng viên phản chứng có người kiểm | Chưa phân công |

### Cổng chuyển W6 → W7

- [ ] Protocol và IC/EC có bản lịch sử trước search chính thức; thay đổi được log.
- [ ] Số liệu PRISMA khớp CSV sau screening/dedup; không có số tự điền.
- [ ] Evidence table có kiểm chéo và mỗi ô quan trọng truy được về nguồn.
- [ ] Mỗi P/I/C/O có bằng chứng hoặc ghi rõ chưa có.
- [ ] Ứng viên phản chứng có người phụ trách, gồm preprint liên quan.
- [ ] Nếu áp dụng đúng học phần: kiểm thêm độ phủ nguồn, ≥12 bài sau gộp và các tỷ lệ/điều kiện trong RBL-1; mọi điều chỉnh ghi rõ trước.

## Week 7 · RBL-2: kiểm chứng RQ

| ID | Việc theo hướng dẫn | Trạng thái | Vị trí đầu ra · điều kiện hoàn tất | Phụ trách · bằng chứng |
|---|---|---|---|---|
| W7-01 | Kiểm evidence table qua P1–P5 | Chưa bắt đầu | `rq-validation.md`: số paper, độ đầy đủ tool/results/limitations/metric theo yêu cầu đã chọn | Chưa phân công |
| W7-02 | Kiểm phản chứng trên từng paper | Chưa bắt đầu | `SLR/<member-id>/rq-check.md`: P/I/C/O, trích đoạn/trang, công trình gần nhất và các nghiên cứu mạnh gần đây | Chưa phân công |
| W7-03 | Ghi gap giả định trước khi đếm và tổng hợp gap | Chưa bắt đầu | `rq-validation.md`: giả định ban đầu có ngày; hạn chế đã/ chưa giải quyết, mẫu số, chất lượng nguồn, loại T/M/D/C | Chưa phân công |
| W7-04 | Viết gap, RQ nháp và câu lợi ích | Chưa bắt đầu | `rq-validation.md`: phát biểu giới hạn trong tập tài liệu đã tìm; ai dùng kết quả, quyết định gì với mọi hướng kết quả | Chưa phân công |
| W7-05 | Rà khả thi đo lường (phần A) | Chưa bắt đầu | Metric/formula/rubric, C chạy trên cùng dữ liệu, H0/H1 đúng đại lượng, ngưỡng/practical effect có căn cứ, N có/N cần | Chưa phân công |
| W7-06 | Rà nguồn lực (phần B) và mini-pilot nếu cần | Chưa bắt đầu | Dataset/tool/compute/annotation/chi phí/giờ; số thực từ thử nghiệm; tách dữ liệu pilot và chính thức | Chưa phân công |
| W7-07 | Chốt kết quả kiểm chứng | Chưa bắt đầu | `rq-validation.md`: novelty label có căn cứ, bảng khác biệt, chọn gap/RQ và lý do; blockers được xử lý | Chưa phân công |

## Week 7 · RBL-3: proposal có thể chạy lại

| ID | Việc theo hướng dẫn | Trạng thái | Vị trí đầu ra · điều kiện hoàn tất | Phụ trách · bằng chứng |
|---|---|---|---|---|
| W7-08 | Chốt bảy yếu tố thiết kế | Chưa bắt đầu | Dataset, tool/I, metric, threshold/practical effect, baseline, pipeline và statistical test có version và nguồn | Chưa phân công |
| W7-09 | Hoàn thiện proposal vận hành | Chưa bắt đầu | `proposal.md`: tám mục RBL-3; RQ chính, sampling/split, annotation, N/K, công bằng, failure policy, CI/tests, stop rule, threats/mitigation, ngân sách | Chưa phân công; `docs/research-proposal.md` là đề cương định hướng |
| W7-10 | Bản tiếng Anh và slide nếu áp dụng | Chưa bắt đầu | `proposal_en.docx`, `../presentation/slides_proposal.pdf`: dữ kiện khớp bản thiết kế; kiểm template/cam kết áp dụng | Chưa phân công |
| W7-11 | Rà soát, phê duyệt và đóng băng | Chưa bắt đầu | Version/commit/tag sau xác nhận cần thiết; checklist đạt, không còn TBD cốt lõi; chưa tự tạo tag phê duyệt | Chưa phân công |
| W7-12 | Theo dõi thay đổi sau đóng băng | Chưa bắt đầu | [Nhật ký](decision-log.md), amendment khi áp dụng; ghi trạng thái đã tiếp xúc dữ liệu và tác động | Chưa có protocol được khóa |

### Cổng kết thúc W7

- [ ] RQ có P/I/C/O cụ thể; so sánh chính và metric chính được xác định.
- [ ] Novelty/gap có evidence, công trình gần nhất đã xác minh; không suy từ reviewer của bài mình sang gap toàn lĩnh vực.
- [ ] Dữ liệu, annotation, baseline và công cụ đo đã thử được trên pilot phù hợp.
- [ ] Có giả thuyết, practical effect/ngưỡng, N/K và kế hoạch phân tích có căn cứ.
- [ ] Development/pilot/test tách rõ, xử lý paraphrase/concept-pair clusters và leakage.
- [ ] Failure policy phân biệt lỗi phương pháp với harness; parser của hệ thống không tự bị loại như lỗi đo.
- [ ] Phiên bản, ngân sách, lịch, trách nhiệm và yêu cầu người tham gia đã rõ.
- [ ] Proposal được rà soát và ghi nhận xác nhận cần thiết trước khi đóng băng.

## Cách cập nhật

1. Gắn ID ở trên vào commit, ví dụ `[W6-02] draft search strings`.
2. Khi đổi trạng thái, thêm đường dẫn bằng chứng, người thực hiện/người rà soát và ngày; bản nháp không được đánh dấu hoàn tất.
3. Ghi quyết định ở [decision-log.md](decision-log.md), nhất là thay phạm vi, query/IC-EC, RQ, metric, dữ liệu hoặc thiết kế.
4. Giữ dữ liệu gốc và provenance; N/A khác 0. Không ghi search count, số paper, agreement hay p-value khi chưa đo.
5. Các hướng dẫn lớp học được tham chiếu, không tự coi là lệnh đăng ký RQ, gửi email, cấp quyền, công bố hoặc áp dụng một lựa chọn nghiên cứu.

Mục tiêu là giữ chuỗi **nguồn → evidence → gap → RQ → protocol → kết quả → claim**. Việc khởi tạo tracker không đánh dấu hoàn tất W6/W7.
