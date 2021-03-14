# 2020_AICUP
Name Entity Recognition in Medical Data Contest

## Requirements

```sh
pip install "kashgari>=1.1,<2.0"
pip install "tensorflow>=1.14,<2.0"
```

### Pre-trained BERT model:
- [Google BERT](https://github.com/google-research/bert)
- [Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm)

### BERT Transfer Learning Framework
- [Kashgari](https://github.com/BrikerMan/Kashgari)

---

## Data
> Data files won't be uploaded due to privacy concerns.

---

### Sample Training Data
<img src="./readme_img/1.PNG" width="450">

---

### Sample Test Data
<img src="./readme_img/2.PNG" width="450">

---

### Output Format
<img src="./readme_img/6.PNG" width="450">

---

## [Name Entity Recognition Introduction](./NER_intro.pptx)
<img src="./readme_img/3.PNG" width="450">

---

## Method

---

### Transfer Learning with pre-trained BERT and add BiLSTM + CRF layer
<img src="./readme_img/4.png" width="450">

---

### Bagging the outputs of all kinds of pre-trained BERT
<img src="./readme_img/5.PNG" width="450">

---

## Result on Public Leader Board

---

### Google BERT Batch Size 24
<img src="./readme_img/7.PNG" width="450">

---

### Google BERT Batch Size 36
<img src="./readme_img/8.PNG" width="450">

---

### Roberta wwm
<img src="./readme_img/9.PNG" width="450">

---

### BERT wwm
<img src="./readme_img/10.PNG" width="450">

---

### Bagging the outputs
<img src="./readme_img/11.PNG" width="450">

---

## Reference
https://www.semanticscholar.org/paper/A-BERT-BiLSTM-CRF-Model-for-Chinese-Electronic-Zhang-Jiang/bd01b18df9a39cdd5c66f44051d62f176e9c8e7e
