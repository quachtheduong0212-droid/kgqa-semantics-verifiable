# SEMANTICS-AWARE AND VERIFIABLE PATH-BASED

# ACADEMIC KNOWLEDGE GRAPH QUESTION ANSWERING

## ĐỀ CƯƠNG NGHIÊN CỨU MỞ RỘNG TỪ EAI FISAT 2026

Quach The Duong, Hoang Duc Tai

Bản nghiên cứu nền: A Lightweight Path-Based Framework for Academic Knowledge Graph Question Answering

Người hướng dẫn: \[Chưa xác định\]

Chương trình: Software Engineering

Đơn vị: FPT University, Ho Chi Minh City, Vietnam

Ngày lập: 13 November 2026  \|  Trạng thái: Research proposal / chưa có kết quả mới

Ghi chú: Bản đề cương tái sử dụng bố cục của Research-proposal-template-APA.docx; không phải bản thảo journal đã hoàn thành.

# 

# Table of Contents \| Mục lục

1\. Introduction \| Giới thiệu

2\. Literature Review \| Tổng quan nghiên cứu

3\. Research Design and Methods \| Thiết kế nghiên cứu và phương pháp

4\. Implications and Contributions to Knowledge \| Đóng góp dự kiến

5\. References \| Tài liệu tham khảo

6\. Research Schedule \| Tiến độ nghiên cứu

Mục lục dạng tĩnh theo cấu trúc template; điều hướng bằng Heading/Document outline trong Google Docs. Số trang có thể thay đổi khi chuyển đổi sang Google Docs.

# 

# 1\. Introduction \| Giới thiệu

## 1.1 Background and Context \| Bối cảnh

Câu hỏi tri thức học thuật thường cần giải thích quan hệ giữa các khái niệm, không chỉ trả về một tài liệu có từ khóa trùng khớp. Knowledge Graph Question Answering (KGQA) có thể khai thác các thực thể và quan hệ để tạo câu trả lời có bằng chứng. Các hệ thống dựa trên mô hình thần kinh hoặc LLM có tiềm năng cao nhưng đòi hỏi năng lực tính toán và quy trình kiểm chứng riêng; các phương pháp symbolic/path-based giúp truy vết đường suy luận, nhưng tính hợp lệ của đường đi không đồng nghĩa với tính đúng đắn ngữ nghĩa của câu trả lời (Diefenbach et al., 2018; Sun & Su, 2026).

Bài đã được chấp nhận tại EAI FISAT 2026 của nhóm tác giả (Quach et al., 2026, bản thảo do tác giả cung cấp) đưa ra một prototype KGQA trên đồ thị con Computer Science Ontology (CSO), so sánh BFS, DFS, Dijkstra và A\*. Đồ thị con có 554 nút, 1.448 cạnh có hướng, 16 cặp truy vấn và 20 lần đo thời gian cho mỗi cặp thuật toán–truy vấn. Kết quả báo cáo BFS có mean runtime 0,123 ms; A\* duyệt ít nút nhất trung bình, nhưng mất thời gian nhiều hơn do overhead. Đây là kết quả cho cấu hình kiểm thử hiện tại, không phải bằng chứng một thuật toán vượt trội nói chung.

Email FISAT ngày 12/11/2026 đề nghị tác giả cân nhắc bản mở rộng tạp chí với khoảng 30–40% nội dung mới, thay tiêu đề/abstract và trích dẫn bản hội nghị. Đây là lời mời gửi bài, không phải quyết định chấp nhận. Trang chính thức của FISAT và special issue EAI xác nhận tạp chí có quy trình nộp/đánh giá riêng (EAI FISAT, 2026; EAI Endorsed Transactions on Internet of Things, 2026).

## 1.2 Problem Statement \| Vấn đề nghiên cứu

Điểm yếu then chốt là sự không tương xứng giữa tuyên bố “Question Answering” và phép đo thực nghiệm: đầu vào kiểm thử phần lớn là cặp source–target đã xác định; metrics chủ yếu gồm path length, path cost, số nút duyệt, runtime, retrieval success và path validity. Chưa có bộ câu hỏi ngôn ngữ tự nhiên được gán nhãn độc lập để đo khả năng hiểu câu hỏi, ánh xạ khái niệm, chọn đường dẫn có ý nghĩa, độ đúng của câu trả lời và độ trung thực của phần giải thích.

Ngoài ra, hai trọng số quan hệ (superTopicOf=1,0; contributesTo=1,5) được lựa chọn thủ công và chưa có kiểm chứng theo đánh giá người dùng. Heuristic A\* là chênh lệch ontology depth, chưa được chứng minh admissible; vì vậy không thể mặc định tính tối ưu. Dữ liệu 554 nút từ một nhánh CSO hạn chế khả năng khái quát. Ba reviewer đồng thời yêu cầu đánh giá QA thực sự, baseline KGQA, sensitivity analysis, scalability và xác định novelty vượt khỏi việc áp dụng bốn thuật toán chuẩn.

## 1.3 Research Questions \| Câu hỏi nghiên cứu

RQ1 — Việc bổ sung tầng hiểu câu hỏi và entity linking ảnh hưởng như thế nào đến answer correctness, coverage và robustness trước diễn đạt tự nhiên trên đồ thị học thuật?

RQ2 — Lựa chọn/kiểm chứng đường đi có xét ngữ nghĩa và khả năng từ chối khi thiếu bằng chứng có cải thiện explanation faithfulness/semantic correctness so với shortest-hop hoặc lowest-cost path hay không?

RQ3 — Kết quả phụ thuộc đến mức nào vào trọng số quan hệ, heuristic, số hop, quy mô và loại đồ thị? Khi nào overhead của tầng ngữ nghĩa được bù bởi cải thiện chất lượng?

RQ4 — Mức độ cải thiện so với baseline phù hợp có đứng vững trên test set độc lập và đánh giá chuyên gia hay không?

## 1.4 Relevance and Importance \| Tầm quan trọng

Mục đích là nâng bài từ proof-of-concept traversal lên nghiên cứu KGQA end-to-end có điều kiện kiểm chứng rõ ràng, phù hợp yêu cầu về tính tái lập và khả năng diễn giải. Không giả định sẵn rằng semantic path ranking là mới hoặc tốt hơn; chỉ giữ một claim sau khi đã xác minh công trình liên quan và kiểm định trên dữ liệu độc lập.

# 

# 2\. Literature Review \| Tổng quan nghiên cứu

## 2.1 Key Concepts, Theories and Studies \| Các công trình nền tảng

KGQA bao gồm question understanding, entity linking, query/path retrieval, answer selection và explanation. Khả năng giải thích bằng đường đi chỉ có ý nghĩa khi các cạnh thực sự hỗ trợ quan hệ được diễn đạt. CSO cung cấp taxonomy khái niệm khoa học máy tính; khi chỉ dùng superTopicOf và contributesTo, cần tránh diễn giải tùy tiện rằng một chuỗi liên kết tạo thành bằng chứng ngữ nghĩa hợp lệ (Salatino et al., 2020).

EmbedKGQA và ReaRev đại diện cho các hướng sử dụng embedding/mô hình học máy để suy luận trên knowledge graph; GraphRAG minh họa xu hướng kết hợp đồ thị với khai thác thông tin. Các phương pháp này tạo bối cảnh về hiệu năng và trade-off nhưng không phải baseline công bằng nếu dùng khác nhiệm vụ, dữ liệu hoặc phần cứng (Saxena et al., 2020; Mavromatis & Karypis, 2022; Edge et al., 2024).

Nghiên cứu PaGLR đã xét path-aware subgraph retrieval và evidence-grounded KGQA bằng GNN–LLM (Sun & Su, 2026). Đặc biệt, preprint HiddenPathQA đưa ra benchmark câu hỏi che giấu chuỗi quan hệ và holistic path selection (Jo & Choi, 2026). Vì vậy ý tưởng “chấm điểm đường đi theo ngữ nghĩa của cả chuỗi” đã có prior art đáng kể; không thể tuyên bố riêng thành phần này là novelty mà không chứng minh khác biệt cốt lõi. HiddenPathQA là preprint mới, tình trạng phản biện/tái lập cần được kiểm tra tiếp.

## 2.2 Key Debates and Controversies \| Các tranh luận

•  Shortest path vs. semantic correctness: đường đi ít hop hoặc cost thấp không nhất thiết biểu thị câu trả lời đúng ngữ nghĩa; cần nhãn độc lập và phân loại lỗi relation composition.

•  Transparent path vs. faithful explanation: việc hiển thị path giúp audit cấu trúc, nhưng chưa chứng minh câu chữ giải thích được hỗ trợ hoàn toàn bởi mỗi cạnh.

•  Lightweight efficiency vs. end-to-end accuracy: runtime đo riêng NetworkX trên đồ thị nhỏ không thể thay thế latency toàn pipeline; phải tính parser, candidate generation, ranking và verbalization.

•  Rule-based robustness vs. generalization: parser regex có thể hoạt động với câu mẫu nhưng dễ thất bại trước câu hỏi tự nhiên, đồng nghĩa và nhập nhằng.

•  Novelty vs. engineering integration: một pipeline ghép sẵn các thuật toán có thể là đóng góp hệ thống, nhưng chưa chắc là đóng góp phương pháp đủ mạnh cho journal.

## 2.3 Gaps in Existing Knowledge \| Khoảng trống cần xác minh

Khoảng trống tiềm năng không phải “chưa ai làm semantic path ranking”; các công trình 2026 bác bỏ phát biểu tuyệt đối này. Khoảng trống khả thi hơn là: (a) đánh giá có kiểm soát tính đúng đắn ngữ nghĩa và tính từ chối trên đồ thị khái niệm học thuật với quan hệ ontology cụ thể; (b) bộ benchmark nhỏ gọn nhưng chất lượng cao, có khó khăn ngôn ngữ tự nhiên và lý giải/nhãn chuyên gia; (c) phân tích trade-off quality–compute giữa symbolic, lightweight semantic ranking và baseline hiện đại. Đây là các giả thuyết về đóng góp, cần systematic prior-art screening trước khi khóa RQ.

# 

# 3\. Research Design and Methods \| Thiết kế và phương pháp

## 3.1 Aims and Objectives \| Mục tiêu

Thiết kế bộ benchmark QA có gold answer, gold evidence/path hoặc nhãn có thể chấp nhận, và câu hỏi no-answer/ambiguous.

Xây baseline end-to-end tái lập từ bản FISAT; định nghĩa rõ input/output và lỗi ở từng thành phần.

Đề xuất một cơ chế kiểm chứng liên kết/đường đi phù hợp ontology học thuật, không mặc định mọi path đều có thể suy diễn hợp lệ.

Đánh giá đầu-cuối, kiểm định thống kê, human annotation, sensitivity, scalability, ablation và efficiency.

Xác định đóng góp cuối cùng theo bằng chứng: phương pháp, bộ đánh giá hoặc kết quả thực nghiệm phủ định có ý nghĩa.

## 3.2 Research Design \| Thiết kế nghiên cứu

Thiết kế thực nghiệm kết hợp định lượng và đánh giá chuyên gia. Giai đoạn A: literature mapping và specification, đóng băng tiêu chí nhãn; B: xây dựng dữ liệu benchmark; C: baseline và đề xuất phương pháp; D: ablation và các thử nghiệm chính; E: human evaluation độc lập, phản biện nội bộ và viết journal. Tránh tối ưu mô hình trên tập kiểm thử cuối; chia phát triển/test theo cặp khái niệm hoặc lớp quan hệ để hạn chế leakage.

Quy mô dự kiến khởi đầu 200–300 câu hỏi tự nhiên, phân bố trên nhiều kiểu truy vấn: single-hop, 2–5 hop, mixed-relation, paraphrase, synonym, ambiguity, out-of-graph và no-answer. Đây là mục tiêu quản trị nghiên cứu, không phải ngưỡng journal hay cỡ mẫu được chứng minh trước. Sau pilot phải tính lại kích thước dựa trên độ khó và độ chính xác của nhãn.

## 3.3 Methods and Sources \| Dữ liệu, công cụ và quy trình

Nguồn dữ liệu: CSO phiên bản được khóa và mô tả cụ thể; các đồ thị con từ nhiều nhánh; và, nếu điều kiện cho phép, một ontology độc lập để đánh giá khả năng chuyển miền. Ghi lại graph version, quy tắc canonicalization, định hướng cạnh, lựa chọn relation, quy tắc pruning, số nút/cạnh theo từng tập, tỷ lệ câu hỏi không có đáp án.

Annotation: mỗi câu hỏi lưu question ID, question text, language, paraphrase group, source/target khi xác định được, relation intent, accepted answers, supporting triples/path(s), answerability, rationale, annotator IDs ẩn danh và adjudication. Hai người gán nhãn độc lập cho một mẫu được thiết kế trước; công bố tỷ lệ đồng thuận và phân tích bất đồng, không gộp đánh giá chủ quan thành “ground truth tuyệt đối”.

Baseline bắt buộc: (B0) exact/rule-based linking \+ shortest-hop BFS \+ verbalization gốc; (B1) exact/rule-based linking \+ weighted Dijkstra; (B2) improved linking \+ Dijkstra, không semantic re-ranking; (B3) candidate path retrieval \+ semantic/relation-aware re-ranking (đề xuất); (B4) no-abstention vs abstention; (B5) một baseline KGQA/retrieval hiện đại trên cùng bộ dữ liệu nếu khả thi. Các baseline LLM cần công bố model version, prompt, token budget và chi phí sử dụng.

Phương pháp đề xuất (chưa xác nhận novelty): question intent \+ typed relation admissibility, kiểm tra semantics của path composition, ranking các candidate paths dựa trên feature có thể diễn giải; cơ chế confidence/abstention khi không đủ bằng chứng. Hệ thống phải trả lại evidence triples và lý do lựa chọn, không tự khẳng định một edge nếu ontology không hỗ trợ.

Trọng số quan hệ: thử nghiệm nhiều cấu hình đã định trước, bao gồm equal weights, weighted defaults 1,0/1,5 và các biến thể sensitivity. Với A\*, phân tích tính chấp nhận được/nhất quán của heuristic; nếu không có chứng minh hoặc điều kiện tối ưu, đánh giá A\* như guided search và đối chiếu cost với Dijkstra.

## 3.4 Evaluation Protocol \| Giao thức đánh giá

## Bảng 1\. Giao thức và metrics đánh giá

• Question understanding

   Metrics / phép thử: Entity-linking accuracy/F1; intent accuracy; coverage theo paraphrase và ambiguity

   Điều kiện báo cáo: Tách parser errors khỏi retrieval errors; báo cáo macro/micro khi thích hợp

• Answer quality

   Metrics / phép thử: Answer accuracy/F1; semantic correctness; answerability; false-answer rate trên no-answer

   Điều kiện báo cáo: Gold answer & annotation protocol độc lập; error taxonomy

• Explanation quality

   Metrics / phép thử: Evidence/path validity; semantic faithfulness; expert usefulness ratings

   Điều kiện báo cáo: Ít nhất hai rater độc lập trên tập mẫu; báo cáo agreement và disagreement

• Efficiency

   Metrics / phép thử: End-to-end latency p50/p95; peak memory; preprocessing cost; tokens/cost nếu có LLM

   Điều kiện báo cáo: Cùng phần cứng, workload, warm-up; thời gian parser \+ retrieval \+ verbalization

• Robustness

   Metrics / phép thử: Theo số hop, relation type, branch, graph size, lexical overlap

   Điều kiện báo cáo: Mẫu test độc lập; sensitivity analysis và ablation

• Statistical validity

   Metrics / phép thử: Confidence intervals; paired comparisons; paired bootstrap khi hợp lý

   Điều kiện báo cáo: Không kết luận ưu thế chỉ từ trung bình hoặc biểu đồ

Các đơn vị đánh giá phải phù hợp nhau: nếu task là câu hỏi “how are two concepts related”, cần chấm tính đúng đắn của quan hệ/diễn giải, không chỉ exact-match một tên thực thể. Các ví dụ có nhiều đường đi hợp lệ phải cho phép tập bằng chứng thay thế; phân biệt graph-valid, semantically-supported và useful.

## 3.5 Response to Reviewers \| Ma trận xử lý nhận xét FISAT

## Bảng 2\. Ma trận phản hồi ba reviewer FISAT

• R\#1, R\#3

   Nhận xét / hạn chế: 554 nodes; 16 source–target queries; thiếu scalability/generalizability

   Bằng chứng cần bổ sung: Multi-scale, multi-branch, natural-language QA benchmark; báo cáo khác biệt tập phát triển/test

• R\#1, R\#2

   Nhận xét / hạn chế: Manual edge weights 1,0 và 1,5 chưa kiểm chứng

   Bằng chứng cần bổ sung: Sensitivity analysis, human/semantic validation và báo cáo độ ổn định

• R\#1, R\#3

   Nhận xét / hạn chế: Thiếu QA end-to-end và robust entity linking

   Bằng chứng cần bổ sung: Question parsing/linking metrics; answer correctness; no-answer cases

• R\#1, R\#3

   Nhận xét / hạn chế: Thiếu đối chứng KGQA; bốn thuật toán chuẩn chưa tạo novelty

   Bằng chứng cần bổ sung: Baselines trên cùng task; ablation; novelty comparison với PaGLR/HiddenPathQA

• R\#2

   Nhận xét / hạn chế: A\* heuristic chưa admissible; path naturalness chưa được chấm

   Bằng chứng cần bổ sung: Optimality caveat/check; human evaluation với rubric

• R\#1

   Nhận xét / hạn chế: Related work thiếu các hướng lightweight/explainable/GraphRAG

   Bằng chứng cần bổ sung: Literature matrix cập nhật đến ngày nộp, phân biệt bài peer-reviewed và preprint

## 3.6 Practical Considerations and Risks \| Rủi ro và giải pháp

•  R1 — Novelty bị prior art che phủ (nghiêm trọng): kiểm tra PaGLR, HiddenPathQA, các phương pháp symbolic/path ranking trước khi lập claim; nếu không còn đóng góp phương pháp, định vị study thành rigorous empirical evaluation/benchmark nếu kết quả đủ mạnh.

•  R2 — Nhãn gold path khó xác lập: cho phép nhiều đường đi được chấp nhận; lưu rationale và quy trình adjudication; không áp đặt một shortest path duy nhất làm gold.

•  R3 — Benchmark leakage/artificiality: thiết kế test set trước và tách theo concept pair, quan hệ, template paraphrase; có câu hỏi tự nhiên từ người viết độc lập.

•  R4 — Human evaluation thiếu chuyên gia: dùng rubric ngắn với ví dụ chuẩn hóa và phân tích inter-rater agreement; ghi hạn chế nếu số người chấm nhỏ.

•  R5 — Khó tái lập/không đủ tài nguyên: lưu môi trường, code, seeds, danh sách query, cấu hình, runtime tổng thể; duy trì một baseline CPU-only và triển khai phương án LLM ở mức tùy chọn.

•  R6 — Journal scope và quy trình xuất bản: xác nhận với editor độ phù hợp special issue, điều kiện phiên bản mở rộng, lịch xử lý sau khi proceedings xuất bản, APC và chính sách tác giả; không diễn giải fast-track thành được nhận.

## 3.7 Submission Readiness Gates \| Điều kiện chốt bài

Gate 1 — Novelty: lập bảng đối chiếu method–evidence–difference với ít nhất các công trình gần nhất; một đóng góp không được mô tả chỉ bằng việc tích hợp các thuật toán chuẩn.

Gate 2 — Validity: có benchmark QA thật, gold annotations, end-to-end metrics, baseline và ablation; tối thiểu một kết quả chính có interval/kiểm định phù hợp.

Gate 3 — Faithfulness: chứng minh đường đi giải thích không chỉ graph-valid mà còn semantic-supported; nêu rõ trường hợp hệ thống phải từ chối.

Gate 4 — Reproducibility: tài liệu dataset, mã/phiên bản, cấu hình và script tạo bảng/biểu đồ; các limitation được viết tương xứng với bằng chứng.

Gate 5 — Editorial compliance: ≥30–40% nội dung nghiên cứu mới theo email, title/abstract khác, trích dẫn hội nghị và bảng novelty delta; kiểm tra guidelines chính thức trước nộp.

# 

# 4\. Implications and Contributions to Knowledge \| Đóng góp dự kiến

## 4.1 Practical Implications \| Giá trị thực tiễn

Một QA pipeline có bằng chứng truy vết được có thể giúp người học và nhà nghiên cứu thăm dò liên hệ giữa các chủ đề khoa học máy tính. Lợi ích chỉ được tuyên bố sau khi đánh giá xem câu trả lời có đúng, dễ hiểu, và hữu ích với người dùng hay không. Nếu giải pháp chạy tốt trên CPU và chi phí thấp hơn baseline được so sánh công bằng, có thể hỗ trợ triển khai trong bối cảnh tài nguyên hạn chế.

## 4.2 Theoretical and Methodological Implications \| Giá trị học thuật

C1 (dự kiến) — Một giao thức QA có ngữ nghĩa ontology với kiểm tra composition/abstention có thể nâng chất lượng của các hệ thống symbolic/path-based; novelty phải được xác minh bằng literature mapping và chứng minh bởi ablation.

C2 (dự kiến) — Benchmark academic concept KGQA với câu hỏi tự nhiên và nhãn giải thích có thể đóng góp một trường hợp nghiên cứu xác thực. Nếu dataset quá nhỏ, cần diễn đạt đúng là curated evaluation set/pilot thay vì benchmark cộng đồng tổng quát.

C3 (dự kiến) — Bằng chứng thực nghiệm có hệ thống về trade-off quality, interpretability và compute trên ontology khái niệm. Kết quả phủ định có thể có giá trị nếu thiết kế nghiên cứu đủ công bằng và phân tích nguyên nhân rõ ràng.

## 4.3 Decision Between Alternative Extension Strategies \| Lựa chọn chiến lược

## Bảng 3\. So sánh các hướng mở rộng bài báo

• A. Minimal

   Nội dung: Thêm số nút/truy vấn, bảng biểu và related work

   Kết luận: Không đủ xử lý QA validity và novelty; không khuyến nghị

• B. Evaluation-driven

   Nội dung: Benchmark QA, parser, baseline, human evaluation, scalability

   Kết luận: Bổ sung validity mạnh; phương pháp mới có thể chưa đủ

• C. Method \+ Evaluation

   Nội dung: Phương án B \+ ontology-aware validation/ranking \+ ablation

   Kết luận: Ưu tiên triển khai có điều kiện: novelty và improvement phải được chứng minh

Kết luận đánh giá: Chọn phương án C như một giả thuyết nghiên cứu có kiểm soát, khởi đầu từ benchmark và baseline trước khi đầu tư vào phương pháp. Không cam kết tỷ lệ hoặc khả năng chấp nhận vì không có dữ liệu đánh giá độc lập của journal.

# 

# 5\. References \| Tài liệu tham khảo

Danh mục tham khảo theo hướng APA; các mục công trình nền được ghi nhận từ bản thảo FISAT, những mục 2026 bổ sung qua website nhà xuất bản/preprint. Kiểm tra lại DOI và metadata khi hoàn tất manuscript.

Computer Science Ontology (CSO). (n.d.). About CSO. https\://cso.kmi.open.ac.uk/about

Diefenbach, D., Lopez, V., Singh, K., & Maret, P. (2018). Core techniques of question answering systems over knowledge bases: A survey. Knowledge and Information Systems, 55(3), 529–569. https\://doi.org/10.1007/s10115-017-1100-y

EAI FISAT. (2026). Call for papers: Publication and journal extension. https\://fisat.eai-conferences.org/2026/call-for-papers/

EAI Endorsed Transactions on Internet of Things. (2026). Intelligent Systems, Emerging AI, and Advanced Technologies — From AI-driven Innovation to FinTech in Emerging Economies \[Special issue\]. https\://publications.eai.eu/index.php/IoT/ISEAIAT

Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Larson, J., & Ness, R. O. (2024). From local to global: A GraphRAG approach to query-focused summarization \[Preprint\]. https\://arxiv.org/abs/2404.16130

Jo, S., & Choi, E. (2026). HiddenPathQA: A benchmark for knowledge graph question answering when questions hide their paths \[Preprint\]. arXiv. https\://arxiv.org/abs/2611.11802

Mavromatis, C., & Karypis, G. (2022). ReaRev: Adaptive reasoning for question answering over knowledge graphs. Findings of the Association for Computational Linguistics: EMNLP 2022, 2447–2458. https\://doi.org/10.18653/v1/2022.findings-emnlp.181

Quach, T. D., Hoang, D. T., Pham, V. D. D., & Nguyen, T. D. (2026). A lightweight path-based framework for academic knowledge graph question answering \[Accepted FISAT 2026 conference manuscript; bibliographic details pending\].

Salatino, A. A., Osborne, F., & Motta, E. (2020). The computer science ontology: A large-scale taxonomy of research areas. In The Semantic Web – ISWC 2020 (pp. 187–205). Springer. https\://doi.org/10.1007/978-3-030-62466-8\_12

Saxena, A., Tripathi, A., & Talukdar, P. (2020). Improving multi-hop question answering over knowledge graphs using knowledge base embeddings. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 4498–4507. https\://doi.org/10.18653/v1/2020.acl-main.412

Sun, Y., & Su, Y. (2026). PaGLR: A path-aware GNN-LLM framework for evidence-grounded multi-hop knowledge graph question answering. Journal of King Saud University Computer and Information Sciences, 38, Article 339\. https\://doi.org/10.1007/s44443-026-00763-x

Tài liệu nội bộ: FISAT 2026 Program Committee. (22 September 2026). Review comments for “A Lightweight Path-Based Framework for Academic Knowledge Graph Question Answering” \[Email nhận xét, không công bố\]. Được sử dụng để xây ma trận phản hồi, không coi là kết quả nghiên cứu xuất bản.

# 

# 6\. Research Schedule \| Tiến độ nghiên cứu

## Bảng 4\. Tiến độ nghiên cứu tới hạn nộp journal

• P0. Prior-art & scope

   Objectives \| Sản phẩm/điều kiện hoàn thành: Literature matrix, claim novelty, verify special issue fit; chốt RQ sơ bộ

   Deadline \| Mốc dự kiến: 30/11/2026

• P1. Benchmark & baseline

   Objectives \| Sản phẩm/điều kiện hoàn thành: Annotator rubric; 200–300 câu hỏi khởi đầu; baseline end-to-end, test split đóng băng

   Deadline \| Mốc dự kiến: 31/12/2026

• P2. Method/prototype

   Objectives \| Sản phẩm/điều kiện hoàn thành: Ontology-aware validation/ranking, linking robustness, sensitivity & heuristic analysis

   Deadline \| Mốc dự kiến: 31/01/2027

• P3. Main experiments

   Objectives \| Sản phẩm/điều kiện hoàn thành: Comparative results, multi-scale, ablation, CI/paired tests, error analysis

   Deadline \| Mốc dự kiến: 28/02/2027

• P4. Human validation & writing

   Objectives \| Sản phẩm/điều kiện hoàn thành: Independent rating, agreement, manuscript rewrite, novelty delta & reproducibility

   Deadline \| Mốc dự kiến: 31/03/2027

• P5. Internal review & submission

   Objectives \| Sản phẩm/điều kiện hoàn thành: Peer-review nội bộ; xác nhận proceedings/APC/guidelines và nộp nếu đủ gates

   Deadline \| Mốc dự kiến: Trước 15/04/2027

Mốc 15/04/2027 là thời hạn bản thảo công bố tại special issue EAI vào ngày kiểm tra 13/11/2026, có thể thay đổi. Cần xác nhận trực tiếp khi bắt đầu quy trình nộp.

Ưu tiên tuần đầu: (1) lập comparison matrix với PaGLR/HiddenPathQA, (2) định nghĩa câu hỏi/nhãn QA, (3) chạy end-to-end baseline trên một tập thử nhỏ, (4) kiểm tra feasibility của độc lập gán nhãn, (5) chỉ sau đó khóa novelty và chọn can thiệp phương pháp.