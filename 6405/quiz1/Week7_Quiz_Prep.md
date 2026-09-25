# EE6405 Week 7 Quiz 预测与复习（Coding Quiz #3）

> **Quiz 形式**：Week 7 是 **Coding Quiz #3**——15 分钟，**5 题单选**，答错**扣分**（near-miss=0 分；完全错答倒扣，总分可为负），闭卷 + Respondus lockdown browser，现场 attendance。
> **覆盖范围**：Coding Quiz #3 **只考前一周（Week 6）的 Transformer 代码**——不考本周新内容、不滚动到更早周（见 `6405_Quiz_Habit_Analysis.md` 时间表）。
> 本文档由 `quiz-predict-6405` skill 生成：从 Week 1–5 quiz 截图/MCQ 归纳出题逻辑，结合 Week 6 notebook（`week6/Week 7.ipynb`）+ Week 6 课件（`EE6405_W4_T_For Students.pdf` + `EE6405_W9_TLLMs_For Students.pdf`）+ `week6/Week7MCQ.md`（本周 practice 题，5 道单选）预测考点。
> ⚠️ **本周 quiz 的 practice 题就是 `week6/Week7MCQ.md` 的 5 题**——notebook 文件名 `Week 7.ipynb` 放在 `week6/` 文件夹里，对应教学 Week 6（Seq2Seq + Attention + Transformer）。`Week7MCQ.md` 也在 `week6/` 下。
> ⚠️ 与 Week 6 IRA/TRA（多选多答概念题）不同，**本周是 Coding Quiz（单选代码题）**——复习重点是**代码 missing-line**，不是概念多选。本文档 §三 的 5 道预测题直接复现 `Week7MCQ.md` 的单选格式。

---

## ⭐ Coding Quiz #3 形式特别提示（区别于 Week 6 IRA/TRA）

- **5 题单选**：每题**只有一个**正确选项（5 选 1），不是多选多答。
- **负分制**：near-miss=0 分（不倒扣）；**完全错答倒扣**（总分可为负）。缩放公式 `(((score*2)+20)/120)*100`（使最低分=0）。
- **全代码题**：Dr. Supraja 的 Coding Quiz 全是"给代码问 missing line / 问输出 / spot error"，无纯概念默写。Week 7 quiz 的代码**逐字摘自 `Week 7.ipynb`**（Week 6 Transformer 类定义）。
- **覆盖只到 W6**：时间表明确 Coding #3(W7) 只考 W6；**不**滚动到 W1–5（与 IRA/TRA 不同）。故 §一 过往知识仅作"万一"的极简提醒，复习重心在 §二 Week 6 代码。
- **应试铁律**：没把握的题选 nearest miss（至少不倒扣）；**完全不会别瞎猜**（瞎猜会倒扣）。

---

## 一、过往知识极简回顾（Week 1–5，大概率不考，仅备查）

> Coding Quiz #3 声明只考 Week 6。但 Supraja 的 quiz 偶有"再之前"知识点滚动复现（见习惯分析）。极简列出，重在辨析，不展开。

### Week 1（Preprocessing）

| 考点 | 一句话 | 易错 |
|---|---|---|
| `PorterStemmer().stem(word)` | 截词尾得 stem | `easily`→`easili` |
| `WordNetLemmatizer().lemmatize(word, pos='v')` | 需 `pos='v'` 才还原动词 | 不传 pos 默认当名词 |
| `re.sub(pattern, repl, string)` | `[^\w\s]` 去标点 | 链式调用记清每步对象 |
| n-gram | `zip(*[words[i:] for i in range(n)])` + `' '.join` | bigram 全列 |

### Week 2（Linguistic Features，spaCy）

| 考点 | 一句话 | 易错 |
|---|---|---|
| `doc.ents` | NER 实体列表 | `doc.entities`（错）vs `doc.ents`（对） |
| `token.pos_` / `token.tag_` | 粗/细粒度 POS | 带下划线，不带是错 |
| `token.dep_` / `token.head.text` | 依赖关系/父节点 | `dep_` 带下划线 |

### Week 3（Term Weighting / Topic Modeling / Dim Reduction）

| 考点 | 一句话 | 易错 |
|---|---|---|
| `CountVectorizer` vs `TfidfVectorizer` | LDA 用 CountVectorizer（整数词频） | LDA 不用 TF-IDF |
| `BM25Okapi(...).get_scores(query)` | 方法名 `get_scores`（**复数**） | `get_score`（单数）错 |
| `PCA` + `.toarray()` | TF-IDF 稀疏矩阵给 PCA 须 `.toarray()` | `n_components`=目标维度 |

### Week 4（Traditional ML，sklearn）

| 考点 | 一句话 | 易错 |
|---|---|---|
| `MultinomialNB`→`GaussianNB` | 改 import + 实例化（2 行） | `.fit/.predict` 通用 |
| `SVC(kernel=..., C=...)` | `C` = 正则强度 | `degree` 属 poly；`gamma` 属 RBF |
| `RBF(length_scale=1.5)` | `length_scale` 传给 `RBF()` 构造器 | 不传分类器 |

### Week 5（Evaluation Metrics + Word Embeddings）

| 考点 | 一句话 | 易错 |
|---|---|---|
| `f1_score(y_true, y_pred, average=...)` | 函数名全小写 | `f1_Score`（大写 S）错 |
| `sentence_bleu([reference], candidate, ...)` | reference 要 **list 包裹** | 不包裹会报错 |
| `Word2Vec(..., sg=0/1)` | `sg=0` CBOW，`sg=1` Skip-gram | `.load` 会覆盖训练模型 |

> 以上 5 周考点在 Week 7 Coding Quiz 中**大概率不出现**（时间表明确只考 W6），但若考场上遇到陌生题，先排查是否为上述 API 的拼写/参数陷阱。

---

## 二、前一周知识详尽讲解（Week 6，Seq2Seq + Attention + Transformer）—— ⭐ 本周 quiz 的唯一考点

> Coding Quiz #3 只考 Week 6 的 Transformer 代码。以下按 `Week 7.ipynb`（`week6/`）+ 课件顺序整理**quiz 会考的类定义**，保留英文术语原词，代码直接摘自 notebook。这是本文档主体。完整概念辨析（AR vs AE、BERT/GPT 等 IRA/TRA 内容）见 `Week6_Quiz_Prep.md` §三——本周是 Coding Quiz，**只考代码 missing-line**，不考概念多选。

### 2.1 ⭐ EncoderRNN / DecoderRNN（notebook cell `2e309038`）

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
        super(DecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)
    def forward(self, encoder_outputs, encoder_hidden, target_tensor=None):
        batch_size = encoder_outputs.size(0)
        decoder_input = torch.empty(batch_size, 1, dtype=torch.long, device=device).fill_(0)
        decoder_hidden = encoder_hidden
        decoder_outputs = []
        for i in range(MAX_LENGTH):
            decoder_output, decoder_hidden = self.forward_step(decoder_input, decoder_hidden)
            decoder_outputs.append(decoder_output)
            if target_tensor is not None:
                decoder_input = target_tensor[:, i].unsqueeze(1)   # teacher forcing
            else:
                _, topi = decoder_output.topk(1)
                decoder_input = topi.squeeze(-1).detach()          # 自回归
        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
        return decoder_outputs, decoder_hidden, None   # ⭐ None for consistency
```

⭐ **关键点**：
- **Teacher forcing**：训练时 `target_tensor is not None` → 用真实 target 作下一步输入；推断时无 target → `topk(1)` 取最大概率词作输入。
- **`return ..., None`**：notebook 注释原文 "for **consistency in the training loop**"——AttnDecoderRNN 返回 `attentions`（第三个返回值），普通 DecoderRNN 为保持调用接口一致返回 `None`。**这是 `Week7MCQ.md` Q1 的答案（选项 3）**。

### 2.2 ⭐ BahdanauAttention（notebook cell `907d4633`）

```python
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super(BahdanauAttention, self).__init__()
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

⭐ **关键点**（`Week7MCQ.md` Q3）：
- `Wa`/`Ua` 是 `nn.Linear(hidden_size, hidden_size)`（保维投影，用于 `tanh(W·q + U·k)`）。
- **`Va` 是 `nn.Linear(hidden_size, 1)`**（投影到 1 维得 score 标量）——这是唯一与 Wa/Ua 不同的层。
- 干扰项把 `Wa`/`Ua` 也设成 `→ 1`（错，只有 Va 输出 1 维）。
- **答案 = 选项 5**（`Wa: hidden→hidden`、`Ua: hidden→hidden`、`Va: hidden→1`）。

### 2.3 ⭐ AttnDecoderRNN（notebook cell `907d4633`）

```python
class AttnDecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p=0.1):
        super(AttnDecoderRNN, self).__init__()
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

⭐ **关键点**（`Week7MCQ.md` Q2）：
- **`self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)`**：GRU 输入维度是 `2 * hidden_size`，因为 `input_gru = torch.cat((embedded, context), dim=2)`——embedding（hidden_size）和 attention context（hidden_size）拼接。
- 完整 `__init__`（在 `self.embedding` 之后、`self.dropout` 之前）应有**三行**：`self.attention` + `self.gru(2*hidden_size)` + `self.out`。
- **答案 = 选项 2**（`attention` + `gru(2*hidden_size, hidden_size)` + `out`）。
- 干扰项：选项 1 缺 gru/out；选项 4 缺 out；选项 5 缺 gru。

### 2.4 ⭐ MultiHeadAttention（notebook cell `0b5bc653`）

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
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

⭐ **关键点**（`Week7MCQ.md` Q4）：
- `W_q`/`W_k`/`W_v`/`W_o` 都是 **`nn.Linear(d_model, d_model)`**（全投影到 `d_model`，再 `split_heads` 拆成多头）。
- **不是** `→ d_k`（选项 2/5）、**不是** `→ num_heads`（选项 4）。
- **答案 = 选项 1**。
- **Scaled dot-product**：`softmax(QK^T / sqrt(d_k)) V`，除以 `sqrt(d_k)` 稳定梯度。
- **Multi-head**：`d_k = d_model // num_heads`；每头独立 attention，concat 再 `W_o` 投影。

### 2.5 ⭐ PositionalEncoding（notebook cell `11bc690b`）

```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)   # ⭐ 偶数维 sin
        pe[:, 1::2] = torch.cos(position * div_term)   # ⭐ 奇数维 cos
        self.register_buffer('pe', pe.unsqueeze(0))
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]   # ⭐ 按输入序列长度截取
```

⭐ **关键点**（`Week7MCQ.md` Q5）：
- **偶数维 sin，奇数维 cos**：`pe[:, 0::2] = sin(...)`、`pe[:, 1::2] = cos(...)`。
- **`forward` 返回 `x + self.pe[:, :x.size(1)]`**——`x.size(1)` 是 **seq_len**（第二维），按序列长度截取 pe。
- `register_buffer('pe', ...)`：pe 非参数（不训练），但随 model 移到 device。
- **答案 = 选项 5**。
- 干扰项：`x.size(0)`（batch_size，错，选项 4）、`self.pe[:x]`（语法错，选项 2）、`return x`（不加 PE，选项 1）、`x + self.pe`（不截取维度不匹配，选项 3）。

### 2.6 PositionWiseFeedForward / EncoderLayer / DecoderLayer（notebook cell `1471af63`–`5cc16eae`）

```python
class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        self.fc1 = nn.Linear(d_model, d_ff); self.fc2 = nn.Linear(d_ff, d_model); self.relu = nn.ReLU()
    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))   # 两线性 + 中间 ReLU

class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model); self.norm2 = nn.LayerNorm(d_model)   # ⭐ 2 个 LayerNorm
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, mask):
        attn_output = self.self_attn(x, x, x, mask)          # ⭐ self-attention: Q=K=V=x
        x = self.norm1(x + self.dropout(attn_output))        # Add & Norm
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))          # Add & Norm
        return x

class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        self.self_attn = MultiHeadAttention(d_model, num_heads)     # masked self-attention
        self.cross_attn = MultiHeadAttention(d_model, num_heads)   # encoder-decoder attention
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model); self.norm2 = nn.LayerNorm(d_model); self.norm3 = nn.LayerNorm(d_model)  # ⭐ 3 个 LayerNorm
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

⭐ **关键点**（潜在 missing-line 题）：
- **EncoderLayer**：2 子层（self-attn + FFN）+ **2 个 LayerNorm**；self-attention Q=K=V=x。
- **DecoderLayer**：3 子层（masked self-attn + cross-attn + FFN）+ **3 个 LayerNorm**；cross-attn Q 来自 decoder、K/V 来自 encoder output。
- **`norm1`/`norm2`/`norm3` 数量**是潜在考点（Encoder 2 个 vs Decoder 3 个）。
- **`self_attn(x, x, x, mask)`**：self-attention 三个输入相同；cross-attn 是 `cross_attn(x, enc_output, enc_output, src_mask)`。

### 2.7 完整 Transformer + generate_mask（notebook cell `35c8e097`）

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

⭐ **关键点**（潜在 missing-line 题）：
- **两种 mask**：**padding mask**（`src != 0` / `tgt != 0`，掩盖 padding 位置）+ **no-peek mask**（`torch.triu` 上三角 `diagonal=1`，防止 decoder 看未来）。
- `tgt_mask = tgt_mask & nopeak_mask`：两者用 `&` 组合。
- 超参 `d_model=512, num_heads=8, num_layers=6, d_ff=2048`（原论文值）。
- 训练：`nn.CrossEntropyLoss(ignore_index=0)` + `optim.Adam(lr=0.0001, betas=(0.9, 0.98), eps=1e-9)`。

### 2.8 本周考点速查表（Coding Quiz #3 核心）

| 类 | 关键点 | `Week7MCQ` 对应 | 答案 |
|---|---|---|---|
| `DecoderRNN.forward` | `return ..., None` for consistency | Q1 | 选项 3 |
| `AttnDecoderRNN.__init__` | attention + `gru(2*hidden_size)` + out | Q2 | 选项 2 |
| `BahdanauAttention.__init__` | `Wa/Ua: hidden→hidden`，`Va: hidden→1` | Q3 | 选项 5 |
| `MultiHeadAttention.__init__` | `W_q/W_k/W_v/W_o: d_model→d_model` | Q4 | 选项 1 |
| `PositionalEncoding.forward` | `x + self.pe[:, :x.size(1)]` | Q5 | 选项 5 |
| `EncoderLayer` | 2 子层 + 2 LayerNorm；Q=K=V=x | 潜在题 | — |
| `DecoderLayer` | 3 子层 + 3 LayerNorm；cross-attn Q=dec,K=V=enc | 潜在题 | — |
| `generate_mask` | padding mask + no-peek mask（`torch.triu`） | 潜在题 | — |
| scaled dot-product | `softmax(QK^T/sqrt(d_k))V` | 潜在题 | — |

---

## 三、⭐ 预测题目（5 道，Coding Quiz 单选风格）

> 本周 quiz 的 practice 题就是 `week6/Week7MCQ.md` 的 5 题——以下**逐题复现**，附答案 + 干扰项陷阱分析。Supraja 的 Coding Quiz 代码**逐字摘自 notebook**，故真题极可能就是这 5 题（选项顺序可能打乱）。每题**单选**（5 选 1），答错倒扣——没把握选 nearest miss，别瞎猜。

### Q1（代码概念）— DecoderRNN 为什么 return None？

**题**（`Week7MCQ.md` Q1）：以下 `DecoderRNN` 的 `forward` 最后 `return decoder_outputs, decoder_hidden, None`，为什么返回 `None`？

```python
return decoder_outputs, decoder_hidden, None
```

选项：
1. for evaluation in the training loop
2. for accuracy in the training loop
3. for consistency in the training loop
4. for uniformity in the training loop
5. None of the above

**答案**：**选项 3**（for consistency in the training loop）

**陷阱分析**：
- notebook 注释原文："return `None` for **consistency in the training loop**"——因为 `AttnDecoderRNN.forward` 返回三个值（`decoder_outputs, decoder_hidden, attentions`），普通 `DecoderRNN` 为保持训练循环中调用接口一致，第三个返回值填 `None`。
- "evaluation / accuracy / uniformity" 均为相近词干扰——核心词是 **consistency**（接口对齐）。
- 选项 5 "None of the above" 是"不知道就选它"的陷阱——但有明确原文，不选。

### Q2（missing line）— AttnDecoderRNN 缺哪几行？

**题**（`Week7MCQ.md` Q2）：`AttnDecoderRNN.__init__` 在 `self.embedding` 之后、`self.dropout` 之前缺了哪几行？

```python
class AttnDecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p=0.1):
        super(AttnDecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        # missing line(s)
        self.dropout = nn.Dropout(dropout_p)
```

选项：
1. `self.attention = BahdanauAttention(hidden_size)`
2. `self.attention = BahdanauAttention(hidden_size)` + `self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)` + `self.out = nn.Linear(hidden_size, output_size)`
3. 选项 2 + `self.linear = nn.Linear(hidden_size, output_size)` + `self.out = nn.Linear(hidden_size, output_size)`（多一个冗余 linear）
4. `self.attention = BahdanauAttention(hidden_size)` + `self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)`（缺 out）
5. `self.attention = BahdanauAttention(hidden_size)` + `self.out = nn.Linear(hidden_size, output_size)`（缺 gru）

**答案**：**选项 2**

**陷阱分析**：
- 完整应有**三行**：`self.attention`（BahdanauAttention）+ `self.gru`（**`2*hidden_size`** 输入，因 `torch.cat((embedded, context))`）+ `self.out`（Linear）。
- ⭐ **`self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)`**——`2 *` 是最大陷阱，漏 `2*` 维度不匹配。
- 选项 3 多了冗余 `self.linear`（notebook 无此层）；选项 4 缺 `self.out`；选项 5 缺 `self.gru`。
- 单选：只选 2。

### Q3（missing line）— BahdanauAttention 缺哪几行？

**题**（`Week7MCQ.md` Q3）：`BahdanauAttention.__init__` 缺了哪几层定义？

```python
class BahdanauAttention(nn.Module):
    def __init__(self, hidden_size):
        super(BahdanauAttention, self).__init__()
        # missing line(s)
```

选项：
1. `Wa: Linear(hidden, hidden)` + `Ua: Linear(hidden, hidden)` + `Va: Linear(hidden, hidden)`
2. `Wa: Linear(hidden, 1)` + `Ua: Linear(hidden, 1)` + `Va: Linear(hidden, 1)`
3. `Wa: Linear(hidden, 1)` + `Ua: Linear(hidden, hidden)` + `Va: Linear(hidden, hidden)`
4. `Wa: Linear(hidden, hidden)` + `Ua: Linear(hidden, 1)` + `Va: Linear(hidden, hidden)`
5. `Wa: Linear(hidden, hidden)` + `Ua: Linear(hidden, hidden)` + `Va: Linear(hidden, 1)`

**答案**：**选项 5**

**陷阱分析**：
- `Wa`/`Ua` 是 `hidden_size → hidden_size`（保维，`tanh(W·q + U·k)`）；**`Va` 是 `hidden_size → 1`**（投影成标量 score）。
- **只有 Va 输出 1 维**——这是 Bahdanau attention 与 MultiHead 的关键区别。
- 选项 1（Va 也 →hidden）错——score 需是标量才能 softmax 成权重。
- 选项 2/3/4 把 Wa 或 Ua 设成 →1，错——只有 Va 输出 1。
- 单选：只选 5。

### Q4（missing line）— MultiHeadAttention 缺哪几行？

**题**（`Week7MCQ.md` Q4）：`MultiHeadAttention.__init__` 在 `self.d_k = d_model // num_heads` 之后缺了哪几行？

选项：
1. `W_q/W_k/W_v/W_o: Linear(d_model, d_model)`
2. `W_q/W_k/W_v/W_o: Linear(d_model, d_k)`
3. `W_q/W_k: Linear(d_model, d_k)` + `W_v/W_o: Linear(d_model, num_heads)`
4. `W_q/W_k/W_v/W_o: Linear(d_model, num_heads)`
5. `W_q/W_k/W_v/W_o: Linear(d_model, self.d_k)`

**答案**：**选项 1**

**陷阱分析**：
- notebook 中 `W_q`/`W_k`/`W_v`/`W_o` **全部** `nn.Linear(d_model, d_model)`，再由 `split_heads` 拆成多头——**不是**投影到 `d_k`（选项 2/5）、**不是**到 `num_heads`（选项 4）。
- 选项 2/5（`→ d_k`）是常见误解（以为每头单独投影到子空间），但 notebook 实现是先投影到全 `d_model` 再 split。
- ⚠️ 注意 `self.d_k`（选项 5）与 `d_k`（选项 2）等价，都是错——投影维度应是 `d_model`。
- 单选：只选 1。

### Q5（missing line）— PositionalEncoding.forward 返回什么？

**题**（`Week7MCQ.md` Q5）：`PositionalEncoding.forward` 应返回什么？

```python
def forward(self, x):
    # missing line(s)
```

选项：
1. `return x`
2. `return self.pe[:x]`
3. `return x + self.pe`
4. `return x + self.pe[:, :x.size(0)]`
5. `return x + self.pe[:, :x.size(1)]`

**答案**：**选项 5**

**陷阱分析**：
- `x + self.pe[:, :x.size(1)]`——`x.size(1)` 是 **seq_len**（第二维），按序列长度截取 pe。
- 选项 4：`x.size(0)` 是 **batch_size**（第一维），错——应截 seq_len 维。
- 选项 1：只返回 `x` 不加 PE，失去位置信息。
- 选项 3：`x + self.pe` 不截取，维度不匹配（pe 是 `max_seq_length`，x 是实际 seq_len）。
- 选项 2：`self.pe[:x]` 语法错（`x` 是 tensor 不能这样切片）。
- 单选：只选 5。

### ⭐ 额外潜在题（若真题不止 5 题或换题，以下类也可能考）

> Supraja 的 Coding Quiz 偶尔会从 notebook 其他类出题。以下备查，万一出现可应对。

**潜在 Q6（missing line）— DecoderLayer cross-attention 调用**：
- `self.cross_attn(x, enc_output, enc_output, src_mask)`——Q=decoder（x）、K=V=encoder output。
- 干扰项：`cross_attn(x, x, enc_output, ...)`（K 应=enc_output 不是 x）、`cross_attn(enc_output, enc_output, x, ...)`（Q/K/V 顺序错）。

**潜在 Q7（概念）— EncoderLayer vs DecoderLayer 的 LayerNorm 数**：
- EncoderLayer **2 个** LayerNorm（`norm1, norm2`）；DecoderLayer **3 个**（`norm1, norm2, norm3`）。
- 干扰项：把两者都设成 2 或 3。

**潜在 Q8（missing line）— generate_mask 的 no-peek mask**：
- `nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool()`
- 关键：`torch.triu(..., diagonal=1)`（上三角不含对角线），`diagonal=0` 会把当前位置也 mask 掉（错）。

---

## 四、复习清单

### 必跑 notebook cell（`week6/Week 7.ipynb`）—— ⭐ 本周 quiz 唯一来源

- [ ] **Cell `2e309038`**：`EncoderRNN`/`DecoderRNN`——teacher forcing、`topk(1)` 自回归、**`return ..., None` 原因**（Q1）。
- [ ] **Cell `907d4633`**：`BahdanauAttention`/`AttnDecoderRNN`——**`Va: →1`**、**GRU 输入 `2*hidden_size`**、`torch.cat((embedded, context))`（Q2/Q3）。
- [ ] **Cell `0b5bc653`**：`MultiHeadAttention`——**四投影全 `→ d_model`**、scaled dot-product 除 `sqrt(d_k)`、`split_heads`/`combine_heads`（Q4）。
- [ ] **Cell `11bc690b`**：`PositionalEncoding`——偶 sin 奇 cos、**`x + self.pe[:, :x.size(1)]`**、`register_buffer`（Q5）。
- [ ] **Cell `1471af63`/`5cc16eae`**：`PositionWiseFeedForward`/`EncoderLayer`/`DecoderLayer`——子层数、LayerNorm 数（2 vs 3）、self-attn vs cross-attn（潜在 Q6/Q7）。
- [ ] **Cell `35c8e097`**：完整 `Transformer` + `generate_mask`——padding mask + no-peek mask（`torch.triu`）（潜在 Q8）。

### 必背 API/参数（精确拼写表）—— ⭐ 负分制下拼写即分数

| API/概念 | 精确写法 | 易错点 | 对应题 |
|---|---|---|---|
| `DecoderRNN.forward` | `return decoder_outputs, decoder_hidden, None` | None = "consistency in the training loop" | Q1 |
| `AttnDecoderRNN.gru` | `nn.GRU(2*hidden_size, hidden_size, batch_first=True)` | 输入 `2*hidden_size`（embedded+context 拼接） | Q2 |
| `BahdanauAttention.Va` | `nn.Linear(hidden_size, 1)` | **只有 Va 输出 1 维**；Wa/Ua 保维 | Q3 |
| `MultiHeadAttention.W_*` | `nn.Linear(d_model, d_model)`（四个全 d_model→d_model） | 不是 →d_k、不是 →num_heads，再 split_heads | Q4 |
| `PositionalEncoding.forward` | `return x + self.pe[:, :x.size(1)]` | 截 `x.size(1)`=seq_len，不是 `x.size(0)` | Q5 |
| `PositionalEncoding` 偶奇 | `pe[:,0::2]=sin`, `pe[:,1::2]=cos` | 偶 sin 奇 cos | Q5 |
| `register_buffer` | `self.register_buffer('pe', pe.unsqueeze(0))` | 非参数，随 device | Q5 |
| `EncoderLayer` | `norm1, norm2`（2 个 LayerNorm）；`self_attn(x,x,x,mask)` | Q=K=V=x | 潜在 |
| `DecoderLayer` | `norm1, norm2, norm3`（3 个 LayerNorm）；`cross_attn(x, enc, enc, src_mask)` | Q=dec, K=V=enc | 潜在 |
| `generate_mask` | `nopeak_mask = 1 - torch.triu(..., diagonal=1).bool()` | `diagonal=1` 不含对角线 | 潜在 |
| scaled dot-product | `attn_scores = Q @ K.transpose(-2,-1) / math.sqrt(self.d_k)` | 除 `sqrt(d_k)`，不是 `d_model` | 潜在 |
| `masked_fill` | `attn_scores.masked_fill(mask == 0, -1e9)` | 把被 mask 位置压成极小 | 潜在 |

### 必背概念辨析（代码题层面）

- [ ] **`return ..., None` 的目的**：consistency——接口对齐 AttnDecoderRNN（它返回 attentions）。
- [ ] **AttnDecoder GRU 输入 `2*hidden_size`**：因 `torch.cat((embedded, context), dim=2)`，embedding 与 context 各 hidden_size。
- [ ] **Bahdanau Va 是 `→1`**：score 需标量才能 softmax 成 attention weight；Wa/Ua 保维。
- [ ] **MultiHead `W_*` 全 `→ d_model`**：先投影到全维再 `split_heads` 拆头，不是直接 `→ d_k`。
- [ ] **`x.size(1)` = seq_len**：PositionalEncoding 按序列长度截取 pe；`x.size(0)` = batch_size 是错。
- [ ] **EncoderLayer 2 LayerNorm / DecoderLayer 3 LayerNorm**：子层数决定（2 子层 vs 3 子层）。
- [ ] **`math.sqrt(self.d_k)`**：scaled dot-product 除 `sqrt(d_k)`，不是 `d_model`、不是 `num_heads`。

### 易错点（干扰项陷阱）—— ⭐ 一眼破

- [ ] `Va: Linear(hidden, 1)` vs `Linear(hidden, hidden)`——只有 Va 输出 1 维（Q3）。
- [ ] MultiHead `W_*: Linear(d_model, d_model)` vs `Linear(d_model, d_k)`——notebook 用全 d_model 再 split（Q4）。
- [ ] `x.size(1)`（seq_len）vs `x.size(0)`（batch_size）——PositionalEncoding 截取（Q5）。
- [ ] GRU 输入 `2*hidden_size`（AttnDecoder 拼接 embedded+context）vs `hidden_size`（Q2）。
- [ ] `return ..., None` = "consistency"——不是 evaluation/accuracy/uniformity（Q1）。
- [ ] `math.sqrt(self.d_k)` 不是 `d_model`（scaled dot-product）。
- [ ] `torch.triu(..., diagonal=1)`——`diagonal=0` 会 mask 当前位置（错）。

---

## 五、应试策略（Coding Quiz #3，单选 + 负分制）

1. **5 题单选，每题一个正确选项**：与 Week 6 IRA/TRA（多选多答）不同——本周**只选一个**。
2. **负分制铁律**：near-miss=0 分（不倒扣），**完全错答倒扣**。没把握的题选 nearest miss（至少不倒扣）；**完全不会别瞎猜**——瞎猜会倒扣，倒扣比不答惨。
3. **代码题先定位 notebook 原文**：Supraja 的 Coding Quiz 代码**逐字摘自 `Week 7.ipynb`**。5 题 = `Week7MCQ.md` 的 5 题（可能打乱选项顺序）。回忆 notebook 类定义即可定位答案。
4. **三类陷阱一眼破**：
   - (a) **维度**：`→ d_model`（MultiHead）vs `→ d_k`（错）vs `→ 1`（Bahdanau Va）。
   - (b) **截取维度**：`x.size(1)`（seq_len，对）vs `x.size(0)`（batch_size，错）。
   - (c) **`2*hidden_size`**：AttnDecoder 的 GRU 输入因拼接 embedded+context。
5. **"为什么 return None"类概念题**：抓关键词 **consistency**（接口对齐），排除 evaluation/accuracy/uniformity。
6. **时间**：15 分钟 5 题 = 每题 3 分钟。先做有把握的（Q2–Q5 都是 missing-line，定位 notebook 即可），概念题（Q1）最后确认。卡住先标记跳过，回来再选 nearest miss。
7. **不确定时的 nearest miss 选择法**：
   - Q2（AttnDecoder）：若记不清 `2*`，至少选含 `attention + gru + out` 三行的选项（选项 2/3），排除缺 gru 或缺 out 的（选项 4/5）。
   - Q3（Bahdanau）：若记不清 Va 维度，选 `Wa/Ua` 都 `hidden→hidden` 的（选项 1/5），排除 Wa/Ua 设成 →1 的。
   - Q4（MultiHead）：若记不清维度，选四个维度一致的（选项 1/2/4），排除混合维度的（选项 3）。
   - Q5（PE forward）：若记不清 `size(1)` vs `size(0)`，选含 `x + self.pe` 的（选项 3/4/5），排除 `return x`（选项 1）和 `self.pe[:x]`（选项 2，语法错）。

---

## 附：Week 1–7 MCQ 真题归纳表（出题逻辑依据）

| 周 | 题型 | 核心 API/概念 | 答案要点 |
|---|---|---|---|
| W1 Q1-5 | 读代码问输出 | `re.sub`/stemming/lemmatization/bigram | s4/`word_tokenize`/选项5/选项1/8 bigram |
| W2 Q1-5 | 读输出 | spaCy `doc.ents`/`pos_`/`dep_` | 全选项1（带下划线） |
| W3 Q1-5 | missing code/调参 | CountVectorizer/BM25/LDA/PCA | `get_scores`复数；LDA用Count |
| W4 Q1-5 | 改模型/调参 | NB/SVM/RBF/LinearRegression/KMeans | Line1&2/C=0.5/RBF(length_scale)/.fit/n_clusters=2 |
| W5 Q1-5 | spot error/选行 | f1_score/AUC/BLEU/Word2Vec/GloVe | Line3,4,8/`metrics.roc_auc_score`/Line2/Line3/`most_similar` |
| W6 | IRA/TRA 多选 | Seq2Seq/Attention/Transformer/LLM 概念 | 见 `Week6_Quiz_Prep.md` §四 |
| **W7 (Coding #3)** | **单选 missing-line** | **只考 W6 Transformer 代码** | **见 §三 Q1-Q5（=`Week7MCQ.md`）** |

> **Week 7 出题规律**：Coding Quiz #3 **只考 Week 6 Transformer 代码**，5 题单选，答案逐字来自 `Week 7.ipynb` 的类定义。practice 题 `Week7MCQ.md` 的 5 题就是真题原型（选项可能打乱）。复习 = 把 `Week 7.ipynb` 的 5 个核心类（DecoderRNN/BahdanauAttention/AttnDecoderRNN/MultiHeadAttention/PositionalEncoding）的定义跑一遍 + 记住每个的"关键维度陷阱"（`2*hidden_size`、`Va→1`、`W_*→d_model`、`x.size(1)`）。

---

> **下一周（Week 8）预告**：Week 8 是 **Mid-term**（35%，监考，覆盖 W1–6）。复习重点 = W1–6 全部知识点（preprocessing → linguistic features → term weighting/topic modeling → traditional ML → evaluation/embeddings → Seq2Seq/Attention/Transformer/LLM）。Coding Quiz #3 之后直接期中，建议考完 Week 7 quiz 即转入 W1–6 全面复习。
