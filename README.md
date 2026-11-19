# Poisson structures on del Pezzo manifolds

**次数1・2の任意次元での Poisson スキーム、族、モジュライ、葉の幾何、形式量子化、零切断の特異点解消。**

2026-11-20（JST） / v1.2

再開時は [研究方針](00_research_plan.md) を最初に読み、[研究ノート](research/research_notes.md)、[公表用原稿](poisson-del-pezzo.tex) の順に進む。正本はこのリポジトリの `main`。原稿は日本語 LuaLaTeX で書く。

## 中心結果

$X$ は滑らかな複素 $n$ 次元 del Pezzo manifold、$n\geq2$、$-K_X=(n-1)H$、$d=H^n\in\{1,2\}$。固定した $X$ 上の Schouten 方程式の零スキームと、それを動く多様体の族へ拡張したモジュライを扱う。

| 次数 | 大域二重ベクトルの次元 | 固定 $X$ 上の Poisson スキーム | 族としての忘却射 |
| --- | --- | --- | --- |
| 1 | $n$ | $\mathbb A^n$ | 階数 $n$ のベクトル束 |
| 2 | $\binom{n+1}{2}$ | $\operatorname{Gr}(2,n+1)$ の Plücker affine cone | 相対 Plücker cone、相対次元 $2n-1$ |

**Jacobi イデアルそのものの一致を、非被約基底を含む任意基底変換と両立させて証明する。** 座標付きの滑らかな係数空間を $U_d$、上表の cone を $\mathfrak C_{d,n}$ とすると、相対 Poisson スキームは $U_d\times\mathfrak C_{d,n}$。座標を忘れる際には非自明な群作用を使う。

$$
\mathcal D_{n,d}=[U_d/G_d],\qquad
\mathcal P_{n,d}=[(U_d\times\mathfrak C_{d,n})/G_d].
$$

これらは有限型・既約の Deligne–Mumford スタックであり、$\mathcal D_{n,d}$ は滑らか、Poisson 構造を忘れる射は **affine・有限表示・平坦**。次数1の全体と次数2の非零部分は滑らかである。次数2の $n\geq3$ では特異点の集合が零切断に一致し、多様体を動かしても零点での二次障害 $Q\wedge Q$ は消えない。曲面では次数1・2の全体が滑らかで、次元はそれぞれ10・9。三次元では37・24となる。

**零切断の幾何：** 次数2の零切断を blow-up した $\mathcal R_{n,2}$ は滑らかな DM スタックで、$\mathcal P_{n,2}$ の非零部分に同型となる。例外因子は相対 $\operatorname{Gr}(2,n+1)$、その法線束は tautological $\mathcal O(-1)$。$n=3$ では五次元二次錐特異点、$n\geq4$ では非局所完全交叉であり、標準方程式 atlas の錐特異点は Gorenstein terminal（頂点 blow-up の discrepancy は $n$）。coarse moduli space の quotient 特異点まで判定したものではない。

基本線束を選べる族 $p:\mathcal X\to T$ では、同変性を担う内在的な公式は

$$
p_*\bigwedge^2T_{\mathcal X/T}
\simeq\bigwedge^{n-1}(p_*H)\otimes
p_*(\omega_{\mathcal X/T}^{-1}\otimes H^{-(n-1)}).
$$

この束は $H$ を基底の線束で捻っても変わらず、基本線束自体の大域的存在を仮定せずに降下する。基本偏極の **クラス** は滑らかな族に一意に定まるため、$\mathcal D_{n,d}$ は基本偏極を別途指定しない多様体のモジュライとも同値である。Poisson 構造の非零部をスカラー倍で割ると、局所的な $\operatorname{Gr}_T(n-1,p_*H)$ の降下を得る。

二重被覆 involution $z\mapsto-z$ は $\pi\mapsto-\pi$ と作用する。これを無視した自明直積としてのモジュライは主張していない。実際の線束のスカラー自己同型、Poisson 構造のスカラー倍、固定多様体の自己同型商を本文で区別する。

非零構造の一般階数は2。標準 ambient stack への一意な延長、一般の部分線型系の一般の葉の閉包として現れる del Pezzo 曲面、曲面の反標準退化因子、中心的超曲面の形式量子化についての既存の証明も本文に保持する。

## 公表原稿と既知結果との区別

[poisson-del-pezzo.tex](poisson-del-pezzo.tex) は、del Pezzo manifold の定義・模型の短いレビューから始まり、固定対象の分類、族、モジュライ、量子化へ進む。旧主原稿の重複は置かない。

曲面の点分類、三次元の LPT の分類、Hong–Xu による曲面の変形次元10・9は既知である。**任意次元・相対 Jacobi スキーム・同変降下の新規性の包括的確認は未了。** 形式量子化には Kontsevich、曲面 potential には Etingof–Ginzburg の定理を用いる。一次資料と適用範囲は [文献メモ](research/literature_notes.md) に記載する。

coarse moduli space の具体的構成、GIT 安定性、特異な多様体を加えたコンパクト化、相対量子化の降下、代数化、全非可換変形の網羅性は未解決として区別する。

## 原稿と研究資産

| ファイル | 役割 |
| --- | --- |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則、現在の到達点、証明の状態、次の着手方法 |
| [poisson-del-pezzo.tex](poisson-del-pezzo.tex) | 日本語 LuaLaTeX の公表用主原稿 |
| [papers/sections/](papers/sections/) | レビュー・分類・幾何・族・モジュライ・量子化の七つの本文ソース（特異点解消を含む） |
| [research/research_notes.md](research/research_notes.md) | 記法、証明の依存、同変性、残る障害 |
| [research/dp4_comparison.md](research/dp4_comparison.md) | 次数4との比較、高階数の例、lift の非一意性、量子化模型 |
| [research/literature_notes.md](research/literature_notes.md)・[references.bib](references.bib) | 一次資料の版・箇所、書誌、既知性の確認範囲 |
| [computations/verify_jacobi.py](computations/verify_jacobi.py) | Casimir・Jacobi・Plücker 係数回収の厳密検算 |
| [computations/verify_families.py](computations/verify_families.py) | 座標変換の character と同時変形の二次障害の厳密検算 |
| [computations/verify_cone.py](computations/verify_cone.py) | 余次元、Plücker 二次式数、discrepancy の整数恒等式を確認（幾何の証明とは別） |
| [docs/reproduction.md](docs/reproduction.md) | 再生成・組版・検証の手順と実行結果 |

```sh
python3 -m pip install -r requirements.txt
make verify
make pdf
```

ルートから `latexmk` だけでも主原稿をビルドできる。LuaLaTeX・LuaTeX-ja・BibTeX・latexmk と Noto CJK フォントを使用し、`build/poisson-del-pezzo.pdf` と SyncTeX を生成する。PDF・中間生成物は Git で追跡しない。GitHub Actions は使わない。

## 関連リポジトリとの分担

- **次数1・2の分類・族・モジュライ**：本リポジトリ。
- **次数3の一般次元 cubic hypersurface**：[nc-cubic](https://github.com/uedakazushi/nc-cubic)。既存の分類・量子化原稿を正本とする。
- **次数4の二次完全交叉**：[poisson-22ci](https://github.com/uedakazushi/poisson-22ci)、[nc-22ci](https://github.com/uedakazushi/nc-22ci)。本repoの比較ノートは詳細分類の代わりではない。
- **次数1の非可換圏の認識・モジュライ**：[nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)。Poisson 構造の量子化と、圏から ambient を認識する問題を区別する。
- **研究全体の入口**：[research-hub](https://github.com/uedakazushi/research-hub)。
