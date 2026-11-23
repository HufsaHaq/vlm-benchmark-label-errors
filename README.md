# Label errors in vision-language benchmarks

  **Status: in progress.** Independent research project by Hufsa Haq (BSc Computer Science, University of Manchester).

  ## The question

  How many items in a widely used vision-language benchmark are wrong or ambiguous, and do model rankings change once they are fixed?

  Benchmark scores decide which vision-language models look best. If a meaningful share of a benchmark's answers are mislabelled, ambiguous or have more than one correct answer, then small differences
  between models may reflect label noise, not ability.
  Northcutt, Athalye and Mueller (2021) found label errors in the test sets of 10 widely used image, text and audio datasets: an average of at least 3.3%, and at least 6% of the ImageNet validation set.
  On ImageNet with corrected labels, ResNet-18 outperforms ResNet-50 if the share of originally mislabelled test examples rises by just 6%.

  That study covered classification. Vision-language benchmarks, where a model answers a question about an image, add new ways for an item to go wrong: a question can be ambiguous, or more than one
  answer can be right. This project measures how often that happens in one widely used benchmark, and whether it changes which models come out on top.

  ## Method (planned)

  1. **Choose one benchmark** that is widely used on vision-language leaderboards, has public labels for the split being audited, and uses multiple-choice or short answers. This includes a novelty check
  (has it been audited already?) and a licence check.
  2. **Write an annotation guideline** before auditing, so every judgement follows the same rules.
  3. **Hand-audit a random sample** of items, with a second annotator on a subset to measure agreement.
  4. **Categorise each problem item**, adapting Northcutt et al.'s categories:
     - **correctable:** the given answer is wrong and a clear correct answer exists;
     - **multi-label:** more than one answer is correct;
     - **neither:** no listed answer is correct;
     - **no agreement:** annotators can't agree, which suggests an ambiguous item.
  5. **Re-score open models** on the original and corrected labels, and test whether their rankings change.
  6. **Release** the corrected labels, the guideline and the code.

  ## What will be released

  - Corrected labels and item IDs. **Not the benchmark's images**, unless its licence allows redistribution.
  - The annotation guideline and agreement statistics.
  - Code to reproduce the re-scoring.

  ## Progress

  - [x] Project scoped
  - [ ] Benchmark chosen (novelty and licence check)
  - [ ] Annotation guideline written
  - [ ] Pilot audit (100 items) with a second annotator
  - [ ] Full audit and re-scoring
  - [ ] Write-up and public release

  ## Reference

  Curtis G. Northcutt, Anish Athalye and Jonas Mueller. *Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks.* NeurIPS 2021 Datasets and Benchmarks Track. arXiv:2103.14749.

  ## Contact

  Hufsa Haq · [github.com/HufsaHaq](https://github.com/HufsaHaq) · [linkedin.com/in/hufsa-haq](https://linkedin.com/in/hufsa-haq)
