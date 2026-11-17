# Semantics-Aware and Verifiable Path-Based Academic KGQA

Repository riêng cho nghiên cứu mở rộng từ bài FISAT 2026:
**Semantics-Aware and Verifiable Path-Based Academic Knowledge Graph Question Answering**.

**Trạng thái:** khởi tạo nghiên cứu từ baseline hiện có. Các thành phần mở rộng bên dưới là kế hoạch; repo chưa có kết quả thực nghiệm mới cho bản journal.

## Tài liệu và nguồn gốc

- [Đề cương nghiên cứu (bản chụp ngày 17/11/2026)](docs/research-proposal.md)
- [Google Docs gốc](https://docs.google.com/document/d/17LCqOgPWKeyUc9AfMtwo1iW9Ionzu0XfaPtBWEdBn6Q/edit?tab=t.0)
- [Repository baseline](https://github.com/egbertbritannia-cpu/kgqa_graph_algorithms)
- [README baseline được lưu lại](docs/baseline-readme.md)
- Baseline commit: 506e4e22b2069b78dc0354336dca576cb2cd4e39
- Bài nền theo đề cương: *A Lightweight Path-Based Framework for Academic Knowledge Graph Question Answering*.

Repo giữ lịch sử commit của baseline. Remote `upstream` trỏ về repo nền; remote `origin` trỏ về repo mở rộng. Bản khởi tạo lấy các file đã commit ở baseline; dữ liệu cục bộ và các file chưa được theo dõi không nằm trong bản khởi tạo.

## Phạm vi mở rộng

1. Question understanding và entity linking cho câu hỏi ngôn ngữ tự nhiên.
2. Kiểm chứng ngữ nghĩa của quan hệ và path composition; trả về evidence triples.
3. Candidate path ranking có xét ngữ nghĩa và cơ chế abstention khi thiếu bằng chứng.
4. Bộ đánh giá QA dự kiến 200–300 câu hỏi, có gold answers/evidence, paraphrase, ambiguity và no-answer.
5. So sánh baseline, ablation, sensitivity, scalability, human evaluation và latency toàn pipeline.

Graph-valid path chưa đồng nghĩa với câu trả lời được hỗ trợ về ngữ nghĩa. Novelty và cải thiện chất lượng cần được kiểm chứng; không mặc định các thành phần dự kiến đã hoạt động.

## Bố cục

- `src/`, `main.py`: code baseline được kế thừa, gồm BFS, DFS, Dijkstra, A*, parser và verbalizer.
- `web/`: giao diện demo baseline.
- `docs/`: đề cương và tài liệu nguồn gốc.
- `manuscript/`: dành cho bản thảo mở rộng.
- `data/raw/`, `data/processed/`: dữ liệu cục bộ, được bỏ qua bởi Git.

## Chạy baseline

Yêu cầu Python 3 và dữ liệu CSO cục bộ. Repo không kèm dữ liệu CSO.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# Đặt CSO.3.5.csv trong data/raw/ trước khi chạy:
.\.venv\Scripts\python.exe src/graph_pruner.py --root data_mining --max-depth 5 --output data/processed/subgraph_data_mining.json
.\.venv\Scripts\python.exe main.py --graph data/processed/subgraph_data_mining.json --question "How is Data Mining related to Random Forests?" --algorithm dijkstra
```

Đây là cách chạy prototype baseline; benchmark và phương pháp mới chưa được triển khai.

## Việc cần làm trước

- [ ] Xác minh prior art và lập bảng đối chiếu novelty.
- [ ] Chốt task, schema câu hỏi, annotation rubric và cách chia development/test.
- [ ] Tái lập baseline end-to-end trên tập pilot.
- [ ] Triển khai linking, path validation/ranking và abstention.
- [ ] Chạy đánh giá có đối chứng, ablation và human evaluation.
- [ ] Viết bản thảo, bảng phần đóng góp mới so với hội nghị và hướng dẫn tái lập.
