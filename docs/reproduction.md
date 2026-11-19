# 再現手順と検証範囲

2026-11-20（JST） / v1.0

## 1. 正本と必要なファイル

正本は GitHub `main` のソースである。[論文](../papers/dp12_poisson.tex) は `papers/sections/` の三つの TeX と [references.bib](../references.bib) を読み込む。[研究方針](../00_research_plan.md) と [研究ノート](../research/research_notes.md) から再開できる。旧原稿や過去の会話を必要としない。

生成 PDF、組版の中間ファイル、検算の標準出力は `build/` に置き、Git の追跡対象から除外する。実行可能な検算コードを残すので、大量の生成出力を保存する必要はない。

## 2. 数学的な確認

今回点検したのは、現行論文に記載した次の論証である。

- weighted Euler 列による大域化、$n=2$ を含むコホモロジー消滅。
- $F$-Casimir 代表への補正、偏微分の正則列と重み制約による全 bivector の記述・一意性。
- Jacobiator の座標公式と、Euler 外積・線型射影による **Jacobi イデアルそのもの**の回収。
- Plücker 関係の straightening、素性、cone の非零部と原点の接空間。
- 内在的 Grassmann 表示、一般階数、葉、曲面の退化因子。
- affine formality の適用条件、内部次数の保存、中心元の持ち上げ、中央商の自由性。
- 曲面の cyclic potential と Rees 構成、追加仮定を明示した AS 中心拡大命題。

これは人が読める証明の論理的点検であり、Lean 等による形式化ではない。Kontsevich・Etingof–Ginzburg などの引用論文の全証明を独立に再証明したものでもない。新規性の包括的確認、相対 Jacobi スキーム、量子化の代数化は未完了。

[次数4比較ノート](../research/dp4_comparison.md) は数学的内容を現行文書へ移して保持したもので、次数4の全主張の全面的独立監査は行っていない。冒頭に個別の確認範囲と文献の未確認点を記載している。

## 3. 厳密な記号検算

Python 3 と SymPy を用いる。今回の実行環境は **Python 3.12.14 / SymPy 1.14.0**。

```sh
python3 -m pip install -r requirements.txt
make verify
```

`computations/verify_jacobi.py` は有理数上の記号多項式を展開する。偏微分 $g_i$ と対称 Hessian $h_{ij}$ は独立な記号として扱い、浮動小数点近似やランダム標本を使わない。

| 対象 | 実行した次元 | 確認内容 | 結果 |
| --- | --- | --- | --- |
| 次数1 | $n=2,3,5$ | Casimir 条件、全座標三組の Jacobi 恒等式 | 成功（49組） |
| 次数2 | $n=2,3,4,5$ | Casimir 条件、$z$ を含む Jacobiator の消滅、$J_{ijk}=2\sum_lq_{ijkl}f_l$ | 成功（69組） |
| 次数2の係数回収 | 同上 | 全ての四添字 Plücker 二次式の回収 | 成功（各次元で0・1・5・15生成元） |
| 零点の変形 | 四つの独立な $x$ 方向 | 階数4の方向の一次変形と二次障害 | 成功 |

計算は、全次元の定理、大域切断の同型、smoothness を入力とする偏微分の独立性、射影的 Jacobi 写像の係数回収の証明を代替しない。任意次元の結論は論文の一般証明による。

## 4. LuaLaTeX 組版

標準環境では TeX Live の LaTeX、LuaTeX、LuaTeX-ja、BibTeX、latexmk と Noto Serif CJK JP / Noto Sans CJK JP を用意する。使用する主なパッケージは `fix-cm`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `bm`, `geometry`, `booktabs`, `longtable`, `array`, `hyperref`, `luatexja-fontspec`。

リポジトリのルートから実行する。

```sh
make pdf
```

出力は `build/dp12_poisson.pdf`。`.latexmkrc` が LuaLaTeX と BibTeX を設定し、相互参照と参考文献を収束させる。

**2026-11-20の組版確認：** LuaHBTeX 1.18.0 と LuaTeX-ja 20250208.0 を用いて `make pdf` が終了コード0で完了した。参考文献を含めて18頁。最終ログで LaTeX エラー、警告、未定義の参照・引用、overfull / underfull box、欠字はなく、BibTeX の警告もなかった。全18頁の画像で配置を確認し、Jacobi イデアルの主定理・証明の頁は拡大して確認した。和文の斜体形がないため正立を使うという Font Info は残るが、表示上の欠落はない。

## 5. 保存時の確認

文書内のローカル参照、TeX の `input` と citation key、必要なファイルの存在を確認する。GitHub へは現行のソースと再現資産を通常コミットで反映し、リモートの tree と内容を確認する。GitHub Actions は使わない。

研究継続用bundleは、Gitで追跡する現行ファイルと、組版済みの `papers/dp12_poisson.pdf` だけを収める。PDFは `make pdf` の出力をこの位置にコピーしたもので、Gitでは追跡しない。ZIPには一つのルートディレクトリを設け、旧版、Gitの履歴、環境修復用ファイル、組版の中間生成物を含めない。配布前にZIPのCRCと、各収録ファイルが確認済みのソース・PDFと一致することを確認する。

原稿生成、数学的点検、計算成功、組版成功、GitHub反映は別々の確認であり、一つの成功を他の成功の証拠にはしない。
