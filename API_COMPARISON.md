# 🤖 Haystack 支援的 LLM API 比較

## 📊 主流 API 比較表

| API 供應商 | 免費額度 | 價格 (每 1M tokens) | 速度 | 品質 | 推薦用途 |
|-----------|---------|-------------------|------|------|---------|
| **Google Gemini** | ✅ 有 | $0.075 (Flash) | ⚡⚡⚡ | ⭐⭐⭐⭐ | 最推薦測試 |
| **Anthropic Claude** | ❌ 無 | $0.80 (Haiku) | ⚡⚡ | ⭐⭐⭐⭐⭐ | 高品質需求 |
| **OpenAI** | ✅ $5 (3個月) | $0.15 (4o-mini) | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 通用推薦 |
| **Cohere** | ✅ 有 | $0.15 (Command-R) | ⚡⚡⭐ | ⭐⭐⭐⭐ | 企業用途 |
| **Ollama** | ✅ 完全免費 | 免費 | ⚡ | ⭐⭐⭐ | 本地部署 |

---

## 🔵 Google Gemini

### ✅ 優點
- **免費額度最慷慨** - 每分鐘 15 次請求免費
- 速度快 (Gemini Flash)
- 支援繁體中文優秀
- 多模態 (文字、圖片、影片)
- Google 帳號即可使用

### ❌ 缺點
- 輸出品質略遜於 GPT-4/Claude
- API 文件較少

### 💰 價格
- **Gemini 1.5 Flash**: $0.075 / 1M input, $0.30 / 1M output
- **Gemini 1.5 Pro**: $1.25 / 1M input, $5.00 / 1M output

### 📦 安裝
```bash
pip install google-generativeai google-ai-generativelanguage
```

### 🔑 取得 API Key
https://aistudio.google.com/app/apikey

### 💻 使用範例
```python
from haystack.components.generators import GoogleAIGeminiGenerator
from haystack.utils import Secret

llm = GoogleAIGeminiGenerator(
    api_key=Secret.from_env_var("GOOGLE_API_KEY"),
    model="gemini-1.5-flash"
)
```

### 🎯 推薦情境
- ✅ 學習和測試
- ✅ 個人專案
- ✅ 需要多模態功能
- ✅ 預算有限

---

## 🟣 Anthropic Claude

### ✅ 優點
- **品質最佳** - 理解力和推理能力強
- 輸出格式穩定
- 支援長上下文 (200K tokens)
- 安全性佳
- 繁體中文表現優秀

### ❌ 缺點
- 無免費額度
- 價格較高 (Pro 版本)
- 速度較慢

### 💰 價格
- **Claude 3.5 Haiku**: $0.80 / 1M input, $4.00 / 1M output
- **Claude 3.5 Sonnet**: $3.00 / 1M input, $15.00 / 1M output
- **Claude 3 Opus**: $15.00 / 1M input, $75.00 / 1M output

### 📦 安裝
```bash
pip install anthropic-haystack
```

### 🔑 取得 API Key
https://console.anthropic.com/

### 💻 使用範例
```python
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
from haystack.utils import Secret

llm = AnthropicChatGenerator(
    api_key=Secret.from_env_var("ANTHROPIC_API_KEY"),
    model="claude-3-5-sonnet-20241022"
)
```

### 🎯 推薦情境
- ✅ 生產環境
- ✅ 需要高品質輸出
- ✅ 複雜推理任務
- ✅ 長文件處理

---

## 🟢 OpenAI

### ✅ 優點
- 生態系統最完整
- 模型選擇多
- 文件豐富
- 社群支援強
- 新帳號有 $5 免費額度

### ❌ 缺點
- 免費額度有時限 (3個月)
- 中國大陸不可用

### 💰 價格
- **GPT-4o-mini**: $0.15 / 1M input, $0.60 / 1M output
- **GPT-4o**: $2.50 / 1M input, $10.00 / 1M output
- **o1-mini**: $3.00 / 1M input, $12.00 / 1M output

### 📦 安裝
```bash
pip install haystack-ai  # 已內建
```

### 🔑 取得 API Key
https://platform.openai.com/api-keys

### 💻 使用範例
```python
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.utils import Secret

llm = OpenAIChatGenerator(
    api_key=Secret.from_env_var("OPENAI_API_KEY"),
    model="gpt-4o-mini"
)
```

### 🎯 推薦情境
- ✅ 通用用途
- ✅ 需要最新功能
- ✅ 豐富的社群資源
- ✅ 企業應用

---

## 🟠 Cohere

### ✅ 優點
- 企業級功能
- 有免費試用額度
- 針對 RAG 優化
- 支援多語言

### ❌ 缺點
- 品質略遜於前三者
- 中文支援一般

### 💰 價格
- **Command-R**: $0.15 / 1M input, $0.60 / 1M output
- **Command-R+**: $2.50 / 1M input, $10.00 / 1M output

### 📦 安裝
```bash
pip install cohere-haystack
```

### 🔑 取得 API Key
https://dashboard.cohere.com/

### 💻 使用範例
```python
from haystack_integrations.components.generators.cohere import CohereChatGenerator
from haystack.utils import Secret

llm = CohereChatGenerator(
    api_key=Secret.from_env_var("COHERE_API_KEY"),
    model="command-r"
)
```

---

## 🖥️ Ollama (本地部署)

### ✅ 優點
- **完全免費**
- 完全離線運行
- 資料隱私最佳
- 無使用限制

### ❌ 缺點
- 需要本地算力
- 品質不如雲端模型
- 速度較慢 (CPU)
- 需要下載大型模型

### 💰 價格
完全免費！

### 📦 安裝
```bash
# 下載 Ollama
# https://ollama.com/download

# 下載模型
ollama pull llama3.2
ollama pull qwen2.5

# 安裝 Haystack 整合
pip install ollama-haystack
```

### 💻 使用範例
```python
from haystack_integrations.components.generators.ollama import OllamaGenerator

llm = OllamaGenerator(
    model="llama3.2",
    url="http://localhost:11434"
)
```

### 🎯 推薦情境
- ✅ 學習測試
- ✅ 資料敏感專案
- ✅ 無網路環境
- ✅ 預算為零

---

## 🎯 選擇建議

### 🆕 **剛開始學習 Haystack?**
**推薦: Google Gemini Flash**
- 免費額度最慷慨
- 速度快
- 品質夠用
- 註冊簡單

### 💼 **生產環境?**
**推薦: Anthropic Claude 3.5 Sonnet**
- 品質最穩定
- 安全性高
- 適合企業應用

### 💰 **預算有限?**
**推薦: Ollama (本地) 或 Gemini Flash**
- Ollama 完全免費
- Gemini Flash 有免費額度且便宜

### 🏢 **企業應用?**
**推薦: OpenAI GPT-4o 或 Claude 3.5**
- 生態完整
- 技術支援好
- 文件豐富

---

## 📝 設定環境變數

### Windows PowerShell
```powershell
# Google Gemini
$env:GOOGLE_API_KEY = "你的API密鑰"

# Anthropic Claude
$env:ANTHROPIC_API_KEY = "sk-ant-xxxxx"

# OpenAI
$env:OPENAI_API_KEY = "sk-proj-xxxxx"

# Cohere
$env:COHERE_API_KEY = "xxxxx"
```

### Linux/Mac
```bash
export GOOGLE_API_KEY="你的API密鑰"
export ANTHROPIC_API_KEY="sk-ant-xxxxx"
export OPENAI_API_KEY="sk-proj-xxxxx"
export COHERE_API_KEY="xxxxx"
```

---

## 🔄 快速切換 LLM

Haystack 的優勢就是可以輕鬆切換不同的 LLM：

```python
# 只需要改這一行！
llm = GoogleAIGeminiGenerator(...)      # Gemini
# llm = AnthropicChatGenerator(...)    # Claude
# llm = OpenAIChatGenerator(...)       # OpenAI
# llm = OllamaGenerator(...)           # Ollama

# Pipeline 其他部分完全不用改
pipeline.add_component("llm", llm)
```

---

## 💡 我的推薦

### 第一次使用
1. **先用 `simple_example.py`** (不需要任何 API)
2. **再用 Google Gemini** (免費額度 + 簡單)
3. **有預算再試 Claude** (品質最好)

### 程式碼在這裡
- `simple_example.py` - 無需 API
- `quickstart_gemini.py` - Google Gemini 版本
- `quickstart_claude.py` - Anthropic Claude 版本
- `quickstart_example.py` - OpenAI 版本

全部都準備好了！選一個開始吧 🚀
