# EE6405 Week 6 Quiz 预测与复习

> **Quiz 形式**：Week 6 是 **IRA/TRA #2（Theory Quiz）**——20 分钟，**多选多答**，错答**扣分**（最低 0），闭卷 + Respondus lockdown browser，现场 attendance。
> 老师声明覆盖 **Week 5 + Week 6**，但实测会带**更早知识点**（见 §一、§二）。
> 本文档由 `quiz-predict-6405` skill 生成：从 Week 1–5 quiz 截图/MCQ 归纳出题逻辑，结合 Week 6 notebook（`week6/Week 7.ipynb`）+ Week 6 课件（`EE6405_W4_T_For Students.pdf` + `EE6405_W9_TLLMs_For Students.pdf`）预测考点。
> ⚠️ **本周 notebook 文件名是 `Week 7.ipynb`，放在 `week6/` 文件夹里**——对应教学 Week 6 内容（Seq2Seq + Attention + Transformer）。`Week7MCQ.md` 也在 `week6/` 下。
> ⚠️ **注意命名错位**：`week6/` 里的 `EE6405_W4_T_*.pdf`（Transformers，Dr. Simon Liu）和 `EE6405_W9_TLLMs_*.pdf`（Transformer-based LLMs，Dr. S. Supraja）共同构成 Week 6 内容。编号（W4/W9）与教学周次不一致，以 folder 为准。

---

## ⭐ IRA/TRA 形式特别提示（区别于 Coding Quiz）

- **多选多答**：每题有**多个正确选项**，每个勾选独立判分（勾对加分、勾错扣分）。
- **错答扣分 ⇒ 不确定的选项宁可不选**：少选不扣分（只是丢分），错选倒扣。
- **先个人（IRA 15%）→ 团队讨论同一题（TRA 5%）**：TRA 阶段可改答案，把有把握的留下。
- **基于 lecture video + slides，不需课外资料**：但仍可能考 notebook 代码层面的"missing code"（见 W4 IRA/TRA 真题全是代码改写）。
- **选项含 always/never/must 的通常不选**，除非课件明确说绝对。
- 本文档预测的 5 题混合**代码题**（沿用 Supraja 的代码改写习惯）+ **概念多选题**（IRA/TRA 特有的概念理解题）。

---

## 一、过往知识精简回顾（Week 1–4，quiz 会滚动复现）

> IRA/TRA 虽声明覆盖 W5+W6，但 Supraja 的 quiz 实测会带"再之前"的知识点。精简列出，重在辨析。

### Week 1 精简（Preprocessing）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **Stemming**（PorterStemmer） | 截词尾得 stem（可能无意义，如 `easili`） | `easily`→`easili` 不是 `easily` |
| **Lemmatization**（WordNetLemmatizer） | 归约到字典 lemma，需 `pos='v'` 才正确还原动词 | 不传 pos 默认当名词 |
| **re.sub / regex** | `[^\w\s]` 去标点（`\w`=词字符、`\s`=空白）；`\W+` 会连空格一起去 | `[^\w\s]` vs `\W+` 是真题陷阱 |
| **N-gram** | 连续 n 个 token；bigram 用 Markov assumption | bigram 全列 |

### Week 2 精简（Linguistic Features，spaCy）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **NER** | `doc.ents`，`entity.text`/`entity.label_` | `doc.entities`（错）vs `doc.ents`（对） |
| **POS tagging** | `token.pos_`（粗粒度）/ `token.tag_`（细粒度） | 带下划线 `pos_`/`tag_`，不带的是错 |
| **Dependency parsing** | `token.dep_`/`token.head.text`/`token.children` | `dep_` 带下划线；`children` 是生成器要 `list()` |

### Week 3 精简（Term Weighting / Topic Modeling / Dim Reduction）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **CountVectorizer vs TfidfVectorizer** | LDA 用 CountVectorizer（整数词频），不用 TF-IDF | LDA 要计数，TF-IDF 是浮点 |
| **BM25** | `BM25Okapi(tokenized_corpus).get_scores(tokenized_query)` | `get_scores`（**复数**），`get_score` 错 |
| **TruncatedSVD / PCA** | LSA 用 TruncatedSVD（稀疏矩阵可接），PCA 要 `.toarray()` | `n_components=3` 才是降到 3 维 |

### Week 4 精简（Traditional ML）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **Naïve Bayes** | `MultinomialNB`→`GaussianNB` 改 import + 实例化（2 行），`.fit/.predict` 通用 | W4 Q1 答案 Line 1 and 2 |
| **SVM** | 调正则强度用 **`C=0.5`**；kernel trick 解线性不可分 | `degree` 属 poly；`gamma` 属 RBF；`coef0` 属 poly/sigmoid |
| **Gaussian Process** | `length_scale` 传给 `RBF()` 构造器，不传分类器 | `length_scale_bounds` 是优化边界 |
| **LinearRegression** | 训练用 `.fit(X, y)` | `.score` 返回 R²；`.compile` 是 Keras |
| **KMeans** | 改簇数用 `n_clusters=2` | `n_init`/`max_iter` 是干扰项 |

---

## 二、前一周稍微丰富（Week 5，Neural Language Models + Hyperparameter Tuning）

> Week 5 是 Week 6 quiz 声明覆盖的"上周"——稍详细，因为必考。本周 notebook `week5/Week 6.ipynb` 代码是 Week 6 Seq2Seq 的直接前置（RNN/LSTM/GRU → 加 encoder-decoder → 加 attention）。

### 2.1 ⭐ RNN / LSTM / GRU（notebook cell 2–9）

三种神经语言模型，结构同构：`Embedding → 循环层 → Linear`。

```python
class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)   # 注意 batch_first
        self.fc = nn.Linear(hidden_dim, output_size)
    def forward(self, x):
        x = self.embedding(x); out, _ = self.rnn(x); out = self.fc(out); return out
```

| 模型 | nn 层 | 关键点 |
|---|---|---|
| **RNN** | `nn.RNN(embedding_dim, hidden_dim, batch_first=True)` | 最简单，梯度消失 |
| **LSTM** | `nn.LSTM(embedding_dim, hidden_dim, batch_first=True)` | 三门（input/forget/output gate）解长程依赖 |
| **GRU** | `nn.GRU(embedding_dim, hidden_dim, batch_first=True)` | 两门（reset/update gate），比 LSTM 简单 |
| **Bi-RNN** | `nn.RNN(..., bidirectional=True)` | `fc` 输入维度 = `hidden_dim * 2`（双向拼接） |

⭐ **易错点**：
- `batch_first=True`：输入 shape 为 `(batch_size, seq_len, embedding_dim)`，否则默认 `(seq_len, batch, ...)`。
- Bi-RNN 的 `nn.Linear` 输入维度是 `hidden_dim * 2`（双向各一 hidden），单向是 `hidden_dim`。
- `out, _ = self.rnn(x)`：RNN/LSTM/GRU 返回 `(output, hidden)`，LSTM 返回 `(output, (h, c))`。
- LSTM 与 GRU 的门数不同（LSTM 3 门 + cell state；GRU 2 门，无 cell state）——概念题高频。

### 2.2 训练循环（notebook cell 11）

```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
for epoch in range(num_epochs):
    optimizer.zero_grad()
    output = model(sequence_data)
    loss = criterion(output.view(-1, vocab_size), target_data.view(-1))
    loss.backward()
    optimizer.step()
```

- **`nn.CrossEntropyLoss()`** = `LogSoftmax + NLLLoss`，用于多分类（注意 W6 Seq2Seq 用 `NLLLoss` + 手动 `log_softmax`）。
- `output.view(-1, vocab_size)`：reshape 给 loss。
- **Adam** `lr=0.01`；`.zero_grad()` 每轮清梯度。

### 2.3 Hyperparameter Tuning（概念，notebook cell 14–16 提及）

- **GridSearch**：穷举所有参数组合；**RandomizedSearch**：随机采样参数空间。
- 常调超参：`learning_rate`、`hidden_dim`/`hidden_size`、`num_layers`、`dropout`、`batch_size`、`num_epochs`。
- 过拟合对策：dropout、正则化（L2/weight decay）、early stopping、减小模型容量。

> Week 6 quiz 可能考"RNN/LSTM/GRU 的门数""Bi-RNN 的 fc 维度""batch_first 含义"这类概念题——见 §四 Q1。

---

## 三、本周知识详尽讲解（Week 6，Seq2Seq + Attention + Transformer + LLMs）

> 按 `Week 7.ipynb`（`week6/`）+ 两份课件 `EE6405_W4_T_For Students.pdf`（Transformers，Dr. Simon Liu）+ `EE6405_W9_TLLMs_For Students.pdf`（Transformer-based LLMs，Dr. S. Supraja）顺序整理，保留英文术语原词。代码直接摘自 notebook（cell 编号对应）。这是文档主体。

### 3.1 Seq2Seq Model（notebook cell 2，对应 W4-T slides 3–4）

- **Sequence-to-Sequence (Seq2Seq)**：输入序列 → 输出序列，用于 machine translation、text summarization、QA。
- **Encoder-Decoder 架构**：
  - **Encoder**：RNN/LSTM/GRU 逐步处理输入序列，输出一个 **context vector**（固定大小向量，捕获输入语义）。
  - **Decoder**：以 context vector 为起点，逐步生成输出序列。
- **信息瓶颈（bottleneck）**：输入序列越长，context vector 越难保留全部信息 → 性能下降。LSTM/GRU 不足以处理很长序列 → **attention 机制**登场。

### 3.2 ⭐ EncoderRNN / DecoderRNN（notebook cell `2e309038`）

```python
class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p=0.1):
        super().__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(dropout_p)
    def forward(self, input):
        embedded = self.dropout(self.embedding(input))
        output, hidden = self.gru(embedded)
        return output, hidden

class DecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size):
        super().__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)
    def forward(self, encoder_outputs, encoder_hidden, target_tensor=None):
        ...
        for i in range(MAX_LENGTH):
            decoder_output, decoder_hidden = self.forward_step(decoder_input, decoder_hidden)
            ...
            if target_tensor is not None:
                decoder_input = target_tensor[:, i].unsqueeze(1)   # teacher forcing
            else:
                _, topi = decoder_output.topk(1)
                decoder_input = topi.squeeze(-1).detach()          # 自回归生成
        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
        return decoder_outputs, decoder_hidden, None   # None for consistency in training loop
```

⭐ **关键点**：
- **Teacher forcing**：训练时 `target_tensor is not None` → 用真实 target 作下一步输入（加速收敛）；推断时无 target → 用 `topk(1)` 取最大概率词作输入（自回归）。
- **`decoder_output.topk(1)`**：取概率最高的词；`.squeeze(-1).detach()`：去维度 + 断梯度（推断时不回传）。
- **`F.log_softmax(decoder_outputs, dim=-1)` + `nn.NLLLoss()`**：等价于 CrossEntropy，但分两步（W5 已学）。
- ⭐ **`return ..., None` 的目的**：notebook 注释原文 "We return `None` for **consistency in the training loop**"——因为 AttnDecoderRNN 返回 `attentions`（第三个返回值），普通 DecoderRNN 为保持调用接口一致返回 `None`。**这是 Week7MCQ Q1 的答案（选项 3）**。

### 3.3 ⭐ Bahdanau Attention（notebook cell `907d4633`，slides 5–9）

**动机**：Seq2Seq 的 bottleneck → attention 让 decoder 直接"看"encoder 所有 hidden state，按相关性加权聚合，不必压缩成一个 context vector。

**三个组件**：**queries (Q)、keys (K)、values (V)**。

```python
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.Wa = nn.Linear(hidden_size, hidden_size)
        self.Ua = nn.Linear(hidden_size, hidden_size)
        self.Va = nn.Linear(hidden_size, 1)      # ⭐ 最后投影到标量（1 维）
    def forward(self, query, keys):
        scores = self.Va(torch.tanh(self.Wa(query) + self.Ua(keys)))
        scores = scores.squeeze(2).unsqueeze(1)
        weights = F.softmax(scores, dim=-1)
        context = torch.bmm(weights, keys)
        return context, weights
```

⭐ **关键公式**（slides 6）：
- **score**：$e_{q,k_i}=q\cdot k_i$（query 与每个 key 的点积）；Bahdanau 版用 `tanh(W·q + U·k)` 再投影到 1 维。
- **attention weight**：$\alpha_{q,k_i}=\text{softmax}(e_{q,k_i})$。
- **attention output**：$\text{attention}(q,K,V)=\sum_i \alpha_{q,k_i}\,v_{k_i}$（加权和）。

⭐ **易错点**（Week7MCQ Q3）：
- `Wa`/`Ua` 是 `nn.Linear(hidden_size, hidden_size)`（保维投影）；
- **`Va` 是 `nn.Linear(hidden_size, 1)`**（投影到 1 维得 score 标量）——这是唯一与 Q2/Q4 不同的层。
- 干扰项把 `Wa`/`Ua` 也设成 `→ 1`（错，只有 Va 输出 1 维）。
- `torch.bmm(weights, keys)`：批量矩阵乘，context = 加权求和。

### 3.4 ⭐ AttnDecoderRNN（notebook cell `907d4633`）

```python
class AttnDecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p=0.1):
        super().__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.attention = BahdanauAttention(hidden_size)
        self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)  # ⭐ 2 * hidden_size
        self.out = nn.Linear(hidden_size, output_size)
        self.dropout = nn.Dropout(dropout_p)
    def forward_step(self, input, hidden, encoder_outputs):
        embedded = self.dropout(self.embedding(input))
        query = hidden.permute(1, 0, 2)
        context, attn_weights = self.attention(query, encoder_outputs)
        input_gru = torch.cat((embedded, context), dim=2)   # ⭐ 拼接 embedded + context
        output, hidden = self.gru(input_gru, hidden)
        output = self.out(output)
        return output, hidden, attn_weights
```

⭐ **关键点**（Week7MCQ Q2）：
- **`self.gru = nn.GRU(2 * hidden_size, hidden_size, ...)`**：GRU 输入维度是 `2 * hidden_size`，因为 `input_gru = torch.cat((embedded, context), dim=2)`——embedding（hidden_size）和 attention context（hidden_size）拼接。
- ⚠️ **不能漏 `self.gru` 和 `self.out`**：Week7MCQ Q2 选项 1 缺 gru/out、选项 4 只有 attention+gru 缺 out、选项 5 缺 gru。完整应是 attention + gru(2*hidden) + out（**选项 2**）。
- `query = hidden.permute(1, 0, 2)`：调 hidden 的维度顺序作 query。

### 3.5 ⭐ Multi-Head Attention（notebook cell `0b5bc653`，slides 22）

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model; self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)   # ⭐ 四个投影都是 d_model → d_model
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)   # ⭐ 除以 sqrt(d_k)
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, -1e9)
        attn_probs = torch.softmax(attn_scores, dim=-1)
        output = torch.matmul(attn_probs, V)
        return output
    def split_heads(self, x):
        batch_size, seq_length, d_model = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)
    def combine_heads(self, x):
        batch_size, _, seq_length, d_k = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)
    def forward(self, Q, K, V, mask=None):
        Q = self.split_heads(self.W_q(Q)); K = self.split_heads(self.W_k(K)); V = self.split_heads(self.W_v(V))
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)
        output = self.W_o(self.combine_heads(attn_output))
        return output
```

⭐ **关键点**：
- **Scaled dot-product attention**：$\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$。**除以 $\sqrt{d_k}$**（slides 19–20：原始 score 除以 8 = $\sqrt{d_k}$，稳定梯度）。
- **Multi-head**：把 `d_model` 拆成 `num_heads × d_k`（`d_k = d_model // num_heads`），每头独立 attention，最后 concat 再 `W_o` 投影。
- ⭐ **Week7MCQ Q4**：`W_q`/`W_k`/`W_v`/`W_o` 都是 **`nn.Linear(d_model, d_model)`**（不是 `→ d_k`、不是 `→ num_heads`）。**答案是选项 1**。干扰项：`→ d_k`（每头投影到子空间看似合理，但 notebook 用 `→ d_model` 再 split_heads）、`→ num_heads`（维度概念错）。
- **mask**：`masked_fill(mask == 0, -1e9)` 把被 mask 位置 score 压成极小 → softmax 后≈0。

### 3.6 ⭐ Positional Encoding（notebook cell `11bc690b`，slides 14）

```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        super().__init__()
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)   # ⭐ 偶数维 sin
        pe[:, 1::2] = torch.cos(position * div_term)   # ⭐ 奇数维 cos
        self.register_buffer('pe', pe.unsqueeze(0))
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]   # ⭐ 按输入序列长度截取
```

⭐ **关键点**：
- **动机**（slides 14）：Transformer 无 recurrence，不天然带顺序信息 → 用 **sinusoidal functions**（不同频率的 sin/cos）给每个位置唯一编码，**加到 embedding 上**。
- **公式**：$PE_{(pos,2i)}=\sin(\frac{pos}{10000^{2i/d_{model}}})$，$PE_{(pos,2i+1)}=\cos(\frac{pos}{10000^{2i/d_{model}}})$。
- **偶数维用 sin，奇数维用 cos**：`pe[:, 0::2] = sin(...)`、`pe[:, 1::2] = cos(...)`。
- **`register_buffer('pe', ...)`**：pe 不参与训练（非参数），但随 model 移动到 device。
- ⭐ **Week7MCQ Q5**：`forward` 返回 `x + self.pe[:, :x.size(1)]`——按输入**序列长度**（`x.size(1)`，第二维 = seq_len）截取 pe。**答案是选项 5**。干扰项：`x.size(0)`（batch_size，错）、`self.pe`（不截取，维度不匹配）、`self.pe[:x]`（语法错）。
- **Transformer-XL 引入 relative positional encoding**（TLLM slides 12）：用 token 间**距离**而非绝对位置。

### 3.7 PositionWise FeedForward / Encoder / Decoder Layers / Transformer（notebook cell `1471af63`–`35c8e097`）

**PositionWiseFeedForward**：
```python
class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        self.fc1 = nn.Linear(d_model, d_ff); self.fc2 = nn.Linear(d_ff, d_model); self.relu = nn.ReLU()
    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))   # 两线性 + 中间 ReLU
```
- 两个线性变换 + ReLU，对每个位置独立作用（升维 d_model→d_ff 再降回）。

**EncoderLayer**（slides 13）：
```python
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model); self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, mask):
        attn_output = self.self_attn(x, x, x, mask)          # ⭐ self-attention: Q=K=V=x
        x = self.norm1(x + self.dropout(attn_output))        # Add & Norm (residual)
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))          # Add & Norm
        return x
```
- **两个子层**：Multi-Head Self-Attention + Feed-Forward，各跟 **Residual Connection + Layer Normalisation**（Add & Norm）。
- **Self-attention**：Q=K=V 都来自同一输入序列（slides 16）——区别于 encoder-decoder attention（Q 来自 decoder，K/V 来自 encoder）。

**DecoderLayer**（slides 23–24）：
```python
class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        self.self_attn = MultiHeadAttention(d_model, num_heads)     # masked self-attention
        self.cross_attn = MultiHeadAttention(d_model, num_heads)   # encoder-decoder attention
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model); self.norm2 = nn.LayerNorm(d_model); self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, enc_output, src_mask, tgt_mask):
        attn_output = self.self_attn(x, x, x, tgt_mask)             # ⭐ masked (tgt_mask)
        x = self.norm1(x + self.dropout(attn_output))
        attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)  # ⭐ Q=dec, K=V=enc
        x = self.norm2(x + self.dropout(attn_output))
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))
        return x
```
- **三个子层**：Masked Self-Attention + Encoder-Decoder (cross) Attention + Feed-Forward，各跟 Add & Norm（**3 个 LayerNorm**）。
- **Masked self-attention**（slides 24）：防止 decoder 看到未来位置（maintain auto-regressive property）。
- **Cross-attention**：Q 来自 decoder 上一层，K/V 来自 encoder output（slides 24）。

**完整 Transformer**（notebook cell `35c8e097`）：
```python
class Transformer(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model, num_heads, num_layers, d_ff, max_seq_length, dropout):
        self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)
        self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
        self.encoder_layers = nn.ModuleList([EncoderLayer(...) for _ in range(num_layers)])
        self.decoder_layers = nn.ModuleList([DecoderLayer(...) for _ in range(num_layers)])
        self.fc = nn.Linear(d_model, tgt_vocab_size)
        self.dropout = nn.Dropout(dropout)
    def generate_mask(self, src, tgt):
        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)                    # padding mask
        tgt_mask = (tgt != 0).unsqueeze(1).unsqueeze(3)
        seq_length = tgt.size(1)
        nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool()  # ⭐ no-peek
        tgt_mask = tgt_mask & nopeak_mask
        return src_mask, tgt_mask
```
- ⭐ **两种 mask**：**padding mask**（`src != 0` / `tgt != 0`，掩盖 padding 位置）+ **no-peek mask**（`torch.triu` 上三角，防止 decoder 看未来）。
- `d_model=512, num_heads=8, num_layers=6, d_ff=2048`（notebook 超参，原论文值）。
- 训练用 `nn.CrossEntropyLoss(ignore_index=0)` + `optim.Adam(lr=0.0001, betas=(0.9, 0.98), eps=1e-9)`。

### 3.8 ⭐ Transformer 优势与关键概念（slides 10, 15–17, 22）

- **"Attention Is All You Need"**（Vaswani et al. 2017）：去除 recurrence/convolution，**纯 attention**，可并行处理。
- **并行性**：不像 RNN 逐步处理，Transformer 一次性处理整个序列 → 训练效率高。
- **Self-attention 示例**："The animal didn't cross the street because **it** was too tired"——self-attention 让模型把 "it" 关联到 "animal"（slides 17）。
- **Residual connection**：缓解 vanishing gradient，支持更深模型。
- **Layer Normalisation**：稳定加速训练。
- **Multi-Head 的意义**（slides 22）：多头并行捕获**不同关系/不同表示子空间**，concat + 线性变换得最终输出，提升 capacity 而不显著增加计算。

### 3.9 ⭐⭐ Transformer-based LLMs（`EE6405_W9_TLLMs`，Dr. Supraja）— 概念题重点

#### (a) Pre-training vs Fine-tuning（slides 5–6）
- **Pre-training**：在大量无标注文本（Wikipedia、Q&A、书）上**无监督**训练，建立通用语言理解基础。
- **Fine-tuning**：在带标签的下游任务（sentiment analysis、text classification、NER）上进一步训练，常需调整模型结构。
- **趋势**：把所有下游任务统一到一个 pre-training 任务（如 T5 把分类也当文本生成）。

#### (b) ⭐ 两种 Pre-training Objectives（slides 8–11，概念高频）

| 类型 | 用哪个 stack | 目标 | 擅长 | 代表 |
|---|---|---|---|---|
| **Autoregressive (AR)** | **decoder** | 前向自回归 $\max\sum \log p_\theta(x_t\|x_1..x_{t-1})$ | **text generation**，pre-train↔fine-tune 一致 | **GPT** 系列 |
| **Autoencoding (AE)** | **encoder** | 随机 mask token 后重建（denoising），$\max\log p_\theta(x_m\|\bar{x}_m)$ | **双向理解**（bidirectional context） | **BERT** |

- **AR 限制**：只能 left-to-right（XLNet 用 permutation 克服）。
- **AE 限制**：假设被 mask 的 token 独立；pre-train（mask 重建）与 fine-tune（生成）存在 **discrepancy**。

#### (c) ⭐ Tokenizer（slides 13–14）
- **Sub-word tokenization**：拆词为 sub-word（root/prefix/suffix），如 "tiresome"→"tire"+"some"、"tired"→"tire"+"d."，让同源词被识别。
- 两种主要方法：
  - **WordPiece**：最大化词汇表数据集似然；BERT 用。
  - **Byte-Pair-Encoding (BPE)**：用全部 256 Unicode 字符，含特殊字符；RoBERTa 用。
  - GPT-2 用 **Byte-level Encoding (BLE)**。

#### (d) ⭐ BERT（slides 15–17）
- **Denoising objective**：随机 mask 15% token。其中 **80% 换 `[MASK]`、10% 换随机词、10% 保持不变**（保持 context）。
- **Next Sentence Prediction (NSP)**：二分类判断两句是否连续（50% 真连续 + 50% 随机）。
- Fine-tuning 四类下游任务：Sentence Pair Classification、Single Sentence Classification、SQuAD QA、NER Tagging。

#### (e) ⭐ BERT Variants（slides 18–20）

| 变体 | 与 BERT 的区别 |
|---|---|
| **RoBERTa** | 去掉 NSP；dynamic masking（每 epoch 重新 mask，BERT 静态）；用 **BPE** 而非 WordPiece；更多数据、更长序列 |
| **DistilBERT** | **knowledge distillation**：小 student 模仿大 teacher（BERT）的 soft label；参数减 40%（encoder 减半），保留 97% 能力，推理快 60% |
| **DistilRoBERTa** | 同 distillation，但 teacher 是 RoBERTa |

#### (f) ⭐ GPT 系列（slides 21–25）
- **GPT-1**（2018, 117M 参数）：仅 decoder stack，左到右 AR，需 fine-tuning，无 emergent capability。
- **GPT-2**（2019, 1.5B）：引入 **in-context learning** 雏形；用 **BLE** tokenizer。
- **GPT-3**（2020, 175B）：强 **in-context learning**（zero-shot / few-shot），无需 fine-tuning 即可比肩 fine-tuned SOTA。
- **GPT-4**（2023, ~1.7T 参数，45TB 数据）：接受**文本 + 图像**输入，更 nuanced。
- **ChatGPT** = GPT-3 + **InstructGPT**（**RLHF** = Reinforcement Learning from Human Feedback）fine-tune。

#### (g) ⭐ In-context learning（slides 24，概念高频）
- **不更新权重**，仅在 prompt 里给 0/1/few 个示例让模型推断模式。
- **Zero-shot**：无示例，仅任务描述。
- **One-shot / Few-shot**：给 1 个 / 少量示例。
- 区别于 fine-tuning（需准备数据集 + 更新权重）。

#### (h) T5 / BART / XLNet（slides 26–29）
- **T5**（Google）：encoder-decoder + denoising；**把所有 NLP 任务统一成 text generation**（含分类）。mask 连续 token 用 sentinel 替换。
- **BART**（Facebook）：encoder-decoder + denoising，类似 T5；mask 30% token + sentence permutation。
- **XLNet**（CMU+Google）：基于 AR 目标 + **所有 permutation 的期望**，兼顾 AE 的双向理解 + AR 的 pre-train/fine-tune 一致性；基于 Transformer-XL（segment recurrence + relative PE）。

#### (i) 总结（slides 30）
- **AE 模型**擅长双向理解；**AR 模型**pre-train 与 fine-tune 一致、擅长生成。
- 模型 scale 到一定程度，pre-trained 模型无需 fine-tuning 即可媲美 SOTA（AR 是未来方向，XLNet 试图结合两者）。

### 3.10 本周考点速查表

| API/概念 | 关键点 | 易错 |
|---|---|---|
| `nn.GRU(input, hidden, batch_first=True)` | AttnDecoder 输入 `2*hidden_size`（embedded+context 拼接） | 漏 `2*` |
| `BahdanauAttention` | `Wa/Ua: →hidden_size`，`Va: →1` | 只有 Va 投影到 1 |
| `MultiHeadAttention` | `W_q/W_k/W_v/W_o` 全 `→ d_model`，再 `split_heads` | 不是 `→ d_k`、不是 `→ num_heads` |
| scaled dot-product | `softmax(QK^T/sqrt(d_k))V` | 除以 `sqrt(d_k)`，不是 `d_model` |
| `PositionalEncoding` | 偶 sin 奇 cos；`forward` 返回 `x + self.pe[:, :x.size(1)]` | 截取用 `x.size(1)`（seq_len） |
| `register_buffer` | pe 非参数但随 device | 不是 `nn.Parameter` |
| EncoderLayer | 2 子层 + 2 LayerNorm；self-attn Q=K=V=x | — |
| DecoderLayer | 3 子层 + 3 LayerNorm；masked self-attn + cross-attn | cross-attn Q=dec, K=V=enc |
| mask | padding mask + no-peek mask（`torch.triu`） | — |
| AR vs AE | AR=decoder/生成；AE=encoder/双向理解 | GPT=AR，BERT=AE |
| BERT mask | 15% 中 80% [MASK] / 10% 随机 / 10% 不变 | 不是全 [MASK] |
| RoBERTa | 去 NSP + dynamic masking + BPE | 与 BERT 区别 |
| in-context learning | zero/one/few-shot，不更新权重 | vs fine-tuning |
| RLHF | ChatGPT = GPT-3 + InstructGPT(RLHF) | — |

---

## 四、⭐ 预测题目（5 道，IRA/TRA 多选多答风格）

> IRA/TRA 是**多选多答**（每题多个正确选项，错答扣分）。以下预测混合**代码改写题**（沿用 Supraja 代码习惯）+ **概念多选题**（IRA 特有）。代码取自 `Week 7.ipynb`。⚠️ **不确定的选项宁可不选**。

### Q1（代码 missing code）— MultiHeadAttention 四个投影层（复现 Week7MCQ Q4）

**题**：以下 `MultiHeadAttention` 类的 `__init__` 中缺失了哪几行？选出**所有**应填入的行。

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        # missing line(s)
```

选项：
```python
1. self.W_q = nn.Linear(d_model, d_model)
2. self.W_k = nn.Linear(d_model, d_model)
3. self.W_v = nn.Linear(d_model, d_model)
4. self.W_o = nn.Linear(d_model, d_model)
5. self.W_q = nn.Linear(d_model, self.d_k)
6. self.W_q = nn.Linear(d_model, num_heads)
```

**答案**：**1, 2, 3, 4**（四个投影全 `d_model → d_model`）

**陷阱分析**：
- notebook 中 `W_q`/`W_k`/`W_v`/`W_o` **全部** `nn.Linear(d_model, d_model)`，再由 `split_heads` 拆成多头——**不是**投影到 `d_k`（选项 5）、**不是**到 `num_heads`（选项 6）。
- 选项 5/6 是常见误解（以为每头单独投影到子空间），但 notebook 实现是先投影到全 `d_model` 再 split。
- ⚠️ 多选题：只勾确定的 1/2/3/4；若不确定 4（W_o 是否也 d_model）也宁可不勾——但 notebook 明确 W_o 也是 `d_model → d_model`。

### Q2（代码 missing code）— BahdanauAttention 的 Va 维度（复现 Week7MCQ Q3）

**题**：以下 `BahdanauAttention` 类中缺失的层是哪些？选出**所有**正确的定义。

```python
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        # missing line(s)
```

选项：
```python
1. self.Wa = nn.Linear(hidden_size, hidden_size)
2. self.Ua = nn.Linear(hidden_size, hidden_size)
3. self.Va = nn.Linear(hidden_size, hidden_size)
4. self.Va = nn.Linear(hidden_size, 1)
5. self.Wa = nn.Linear(hidden_size, 1)
```

**答案**：**1, 2, 4**（`Wa`/`Ua` 保维 `hidden_size→hidden_size`，`Va` 投影到 `1` 维）

**陷阱分析**：
- `Wa`/`Ua` 是 `hidden_size → hidden_size`（保维，用于 `tanh(W·q + U·k)`）。
- **`Va` 是 `hidden_size → 1`**（投影成标量 score）——这是 Bahdanau attention 与 MultiHead 的关键区别。
- 选项 3（`Va → hidden_size`）错——score 需是标量才能 softmax 成权重。
- 选项 5（`Wa → 1`）错——只有 Va 输出 1 维。
- ⚠️ 选 1/2/4；不选 3/5。若不确定 Va 维度，至少勾 1/2（Wa/Ua 必保维）。

### Q3（概念多选）— Autoregressive vs Autoencoding 模型（IRA 概念题）

**题**：关于 Transformer-based 大语言模型的 pre-training objectives，下列说法**正确**的有？（多选）

1. Autoregressive (AR) 模型主要使用 decoder stack，擅长 text generation。
2. Autoencoding (AE) 模型使用 denoising objective，支持 bidirectional context understanding。
3. GPT 系列属于 Autoencoding 模型。
4. BERT 的 mask 策略中，被选中的 15% token 全部替换为 `[MASK]`。
5. AR 模型的 pre-training 与 fine-tuning 之间存在较少 discrepancy。

**答案**：**1, 2, 5**

**陷阱分析**：
- 1 ✓：AR 用 decoder，前向自回归，擅长生成（slides 9）。
- 2 ✓：AE 用 denoising（mask + 重建），允许双向处理，擅长理解（slides 11）。
- 3 ✗：**GPT 是 AR 模型**（仅 decoder stack），不是 AE——BERT 才是 AE。这是高频混淆点。
- 4 ✗：BERT 的 15% 中 **80% 换 [MASK]、10% 换随机词、10% 保持不变**，不是全部 [MASK]（slides 15）。
- 5 ✓：AR 的 pre-train（生成）与 fine-tune（生成）一致，**discrepancy 小**；AE 的 mask 重建与生成任务有 discrepancy（slides 11）。
- ⚠️ 只勾 1/2/5；3/4 是典型干扰（GPT≠AE；BERT mask 不是全 [MASK]）。

### Q4（代码 missing code）— PositionalEncoding forward 截取（复现 Week7MCQ Q5）

**题**：以下 `PositionalEncoding` 的 `forward` 方法应返回什么？选出**所有**正确的描述。

```python
def forward(self, x):
    # missing line(s)
```

选项：
```python
1. return x + self.pe[:, :x.size(1)]
2. return x + self.pe[:, :x.size(0)]
3. return x
4. return self.pe[:, :x.size(1)]
5. 应按输入序列长度（第二维 seq_len）截取 positional encoding
```

**答案**：**1, 5**（代码 1 + 描述 5 都对）

**陷阱分析**：
- 1 ✓：`x + self.pe[:, :x.size(1)]`——`x.size(1)` 是 **seq_len**（第二维），按序列长度截取 pe，notebook 原文。
- 2 ✗：`x.size(0)` 是 **batch_size**（第一维），错——应截 seq_len 维。
- 3 ✗：只返回 `x` 不加 positional encoding，失去位置信息。
- 4 ✗：只返回 pe 不加 x，失去 token embedding。
- 5 ✓：描述"按输入序列长度（第二维）截取"——与 1 等价的概念表述。
- ⚠️ 多选：勾 1 和 5（代码 + 描述都正确）；不勾 2/3/4。

### Q5（概念多选）— Transformer 架构与注意力（IRA 概念题）

**题**：关于 Transformer 模型，下列说法**正确**的有？（多选）

1. Transformer 不依赖 recurrence 或 convolution，可并行处理整个序列。
2. Self-attention 中 query、key、value 都来自同一输入序列。
3. Decoder 的 masked self-attention 防止位置看到后续位置，保持 auto-regressive 性质。
4. Multi-Head Attention 中每个头使用相同的投影矩阵。
5. Positional encoding 用 sinusoidal 函数为每个位置提供唯一表示。

**答案**：**1, 2, 3, 5**

**陷阱分析**：
- 1 ✓："Attention Is All You Need"——去除 recurrence/convolution，并行处理（slides 10, 22）。
- 2 ✓：self-attention 的 Q=K=V 都来自同一序列（slides 16）——区别于 cross-attention（Q 来自 decoder，K/V 来自 encoder）。
- 3 ✓：masked self-attention 防 decoder 看未来，maintain auto-regressive（slides 24）。
- 4 ✗：**每个头有独立投影**（`W_q`/`W_k`/`W_v` 各自学习不同表示），不是相同矩阵——multi-head 的意义就在"不同头捕获不同关系"。
- 5 ✓：positional encoding 用 sin/cos（slides 14）。
- ⚠️ 勾 1/2/3/5；4 是干扰（多头独立投影，非共享）。

---

## 五、复习清单

### 必跑 notebook cell（`week6/Week 7.ipynb`）

- [ ] **Cell `2e309038`**：`EncoderRNN`/`DecoderRNN`——teacher forcing、`topk(1)` 自回归、`return None` 原因。对照 Week7MCQ Q1。
- [ ] **Cell `907d4633`**：`BahdanauAttention`/`AttnDecoderRNN`——`Va: →1`、GRU 输入 `2*hidden_size`、`torch.cat((embedded, context))`。对照 Week7MCQ Q2/Q3。
- [ ] **Cell `0b5bc653`**：`MultiHeadAttention`——四投影全 `→ d_model`、scaled dot-product 除 `sqrt(d_k)`、`split_heads`/`combine_heads`。对照 Week7MCQ Q4。
- [ ] **Cell `11bc690b`**：`PositionalEncoding`——偶 sin 奇 cos、`x + self.pe[:, :x.size(1)]`、`register_buffer`。对照 Week7MCQ Q5。
- [ ] **Cell `5cc16eae`/`81934a0c`**：`EncoderLayer`/`DecoderLayer`——子层数、LayerNorm 数、self-attn vs cross-attn。
- [ ] **Cell `35c8e097`**：完整 `Transformer` + `generate_mask`——padding mask + no-peek mask。
- [ ] **Cell `109b8123`/`b534530e`/`ce6c8073`**：训练循环——`NLLLoss`/`CrossEntropyLoss(ignore_index=0)`、Adam 超参。

### 必背 API/参数（精确拼写表）

| API/概念 | 精确写法 | 易错点 |
|---|---|---|
| GRU (AttnDecoder) | `nn.GRU(2*hidden_size, hidden_size, batch_first=True)` | 输入 `2*hidden_size`（embedded+context） |
| BahdanauAttention | `Wa/Ua: Linear(hidden, hidden)`, `Va: Linear(hidden, 1)` | 只有 Va 输出 1 维 |
| MultiHead 投影 | `W_q/W_k/W_v/W_o: Linear(d_model, d_model)` | 全 → d_model，再 split_heads |
| scaled dot-product | `attn_scores = Q @ K.transpose(-2,-1) / sqrt(d_k)` | 除 `sqrt(d_k)`，masked_fill(-1e9) |
| PositionalEncoding | `pe[:,0::2]=sin`, `pe[:,1::2]=cos`; `x + pe[:, :x.size(1)]` | 截 `x.size(1)`=seq_len |
| register_buffer | `self.register_buffer('pe', pe.unsqueeze(0))` | 非参数，随 device |
| EncoderLayer | `norm1, norm2`（2 个 LayerNorm） | self-attn Q=K=V=x |
| DecoderLayer | `norm1, norm2, norm3`（3 个 LayerNorm） | cross-attn Q=dec, K=V=enc |
| mask | `src_mask = (src != 0)`; `nopeak_mask = 1 - torch.triu(..., diagonal=1)` | padding + no-peek |
| CrossEntropyLoss | `nn.CrossEntropyLoss(ignore_index=0)` | ignore padding |

### 必背概念辨析（IRA/TRA 概念题）

- [ ] **Seq2Seq bottleneck**：context vector 难保留长序列信息 → attention 解决。
- [ ] **Self-attention vs cross-attention**：self-attn Q=K=V 同序列；cross-attn Q 来自 decoder，K/V 来自 encoder。
- [ ] **Scaled dot-product**：除 $\sqrt{d_k}$ 稳定梯度（slides：除以 8 = $\sqrt{d_k}$）。
- [ ] **Multi-head**：多头并行捕获不同关系，concat + W_o，独立投影（非共享）。
- [ ] **Positional encoding**：sin/cos 不同频率，加到 embedding，给无 recurrence 的 Transformer 位置信息。
- [ ] **AR vs AE**：AR（decoder/生成/GPT）vs AE（encoder/双向理解/BERT）。
- [ ] **BERT mask**：15% 中 80% [MASK] / 10% 随机 / 10% 不变；+ NSP。
- [ ] **RoBERTa**：去 NSP + dynamic masking + BPE。
- [ ] **In-context learning**：zero/one/few-shot，不更新权重（vs fine-tuning 更新权重）。
- [ ] **RLHF**：ChatGPT = GPT-3 + InstructGPT(RLHF)。
- [ ] **T5**：统一所有任务为 text generation；BART：30% mask + sentence permutation；XLNet：permutation AR + Transformer-XL。

### 易错点（干扰项陷阱）

- [ ] `Va: Linear(hidden, 1)` vs `Linear(hidden, hidden)`——只有 Va 输出 1 维。
- [ ] MultiHead `W_*: Linear(d_model, d_model)` vs `Linear(d_model, d_k)`——notebook 用全 d_model 再 split。
- [ ] `x.size(1)`（seq_len）vs `x.size(0)`（batch_size）——PositionalEncoding 截取。
- [ ] GRU 输入 `2*hidden_size`（AttnDecoder 拼接 embedded+context）vs `hidden_size`。
- [ ] `return ..., None`——为 "consistency in the training loop"（接口对齐 AttnDecoder）。
- [ ] GPT 是 **AR** 不是 AE；BERT 是 **AE**。
- [ ] BERT mask 不是全 [MASK]（80/10/10）。
- [ ] Multi-head 各头**独立投影**，不是共享矩阵。
- [ ] `math.sqrt(self.d_k)` 不是 `d_model`。

---

## 六、应试策略（IRA/TRA 多选多答 + 扣分制）

1. **多选多答 ⇒ 不确定的选项宁可不选**：少选只丢分，错选倒扣。这是与 Coding Quiz 最大的区别。
2. **先个人做（IRA），再团队讨论（TRA）**：TRA 阶段可改答案，把有把握的留下，没把握的与团队核对。
3. **概念题看绝对词**：选项含 "always/never/must/all" 通常**不选**，除非课件明确说绝对（如 "d_model must be divisible by num_heads" 是 assert 原文，可选）。
4. **代码题先定位 notebook 原文**：Supraja 的代码题答案几乎都在 notebook 里——回忆 `Week 7.ipynb` 的类定义。
5. **两类陷阱一眼破**：(a) 维度（`→ d_model` vs `→ d_k` vs `→ 1`）；(b) 截取维度（`x.size(1)` vs `x.size(0)`）。
6. **AR/AE/GPT/BERT 辨析**：这是本周概念题最可能的考点——记 GPT=AR(decoder)、BERT=AE(encoder)。
7. **时间**：20 分钟 5 题（多选），每题 4 分钟。先勾确定的，难题留团队讨论。

---

## 附：Week 1–6 MCQ 真题归纳表（出题逻辑依据）

| 周 | 题型 | 核心 API/概念 | 答案要点 |
|---|---|---|---|
| W1 Q1-5 | 读代码问输出 | `re.sub`/stemming/lemmatization/bigram | s4/`word_tokenize`/选项5/选项1/8 bigram |
| W2 Q1-5 | 读输出 | spaCy `doc.ents`/`pos_`/`dep_` | 全选项1（带下划线） |
| W3 Q1-5 | missing code/调参 | CountVectorizer/BM25/LDA/PCA | `get_scores`复数；LDA用Count |
| W4 Q1-5 | 改模型/调参 | NB/SVM/RBF/LinearRegression/KMeans | Line1&2/C=0.5/RBF(length_scale)/.fit/n_clusters=2 |
| W5 Q1-5 | spot error/选行 | f1_score/AUC/BLEU/Word2Vec/GloVe | Line3,4,8/`metrics.roc_auc_score`/Line2/Line3/`most_similar` |
| **W6** | **IRA/TRA 多选** | **Seq2Seq/Attention/Transformer/LLM** | **见 §四 Q1-Q5** |
| W7 (Coding #3) | — | 只考 W6（Transformer 代码） | Week7MCQ Q1-Q5 |

> **Week 6 出题规律预测**：IRA/TRA #2 会混合 (a) **代码 missing-code 题**（沿用 Week7MCQ 的 Transformer 代码：MultiHead/Bahdanau/PE/DecoderRNN）；(b) **概念多选题**（AR vs AE、BERT/GPT 区别、in-context learning、Transformer 架构特点）。复习时把 `Week 7.ipynb` 的类定义跑一遍 + 把两份 PDF 的概念辨析记牢。

---

> **下一周（Week 7）预告**：Week 7 是 **Coding Quiz #3**（只考 Week 6 的 Transformer 代码），15 分钟 5 题单选负分制。复习重点 = `Week 7.ipynb` 全部类定义 + Week7MCQ.md 的 5 题（已归档在本文件夹）。本文档 §三/§四 的代码部分直接适用于 Week 7 Coding Quiz。
