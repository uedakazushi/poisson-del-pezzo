# Poisson structures on del Pezzo manifolds

**次数1・2の任意次元での Poisson スキーム、族、粗モジュライの平坦領域、零切断の特異性と解消。** 葉の幾何・曲面退化・形式量子化の有効な成果も現行原稿に保持する。

2026-11-20（JST） / v1.3

再開時は [研究方針](00_research_plan.md) を最初に読み、[研究ノート](research/research_notes.md)、[公表用原稿](papers/poisson-del-pezzo.tex) の順に進む。正本はこのリポジトリの `main`。原稿は日本語 LuaLaTeX で書く。

## 中心結果

$X$ は滑らかな複素 $n$ 次元 del Pezzo manifold、$n\geq2$、$-K_X=(n-1)H$、$d=H^n\in\{1,2\}$。固定した $X$ 上の Schouten 方程式の零スキームと、それを動く多様体の族へ拡張したモジュライを扱う。

| 次数 | 大域二重ベクトルの次元 | 固定 $X$ 上の Poisson スキーム $C_{d,n}$ | スタックの忘却射 |
| --- | --- | --- | --- |
| 1 | $n$ | $\mathbb A^n$ | 階数 $n$ のベクトル束 |
| 2 | $\binom{n+1}{2}$ | $\operatorname{Gr}(2,n+1)$ の Plücker affine cone | 相対 Plücker cone、相対次元 $2n-1$ |

**Jacobi イデアルそのものの一致を、非被約基底を含む任意基底変換と両立させて証明する。** 座標付きの滑らかな係数空間を $U_d$ とすると、相対 Poisson スキームは $U_d\times C_{d,n}$。座標を忘れる際には、本文で計算した群作用を使う。

$$
\mathcal D_{n,d}=[U_d/G_d],\qquad
\mathcal P_{n,d}=[(U_d\times C_{d,n})/G_d].
$$

これらは有限型・既約で、**有限対角を持つ分離的な Deligne–Mumford スタック**である。滑らかな係数領域 $U_d$ の affine 性と Luna の定理から、全滑らか領域の affine 粗モジュライ空間を構成する。$A_d=\mathcal O(U_d)$、$R_{d,n}=\mathcal O(C_{d,n})$ として

$$
M_{n,d}=\operatorname{Spec} A_d^{G_d},\qquad
N_{n,d}=\operatorname{Spec}(A_d\otimes R_{d,n})^{G_d}.
$$

$\mathcal D_{n,d}$ は滑らかで、**スタックの忘却射** $\mathcal P_{n,d}\to\mathcal D_{n,d}$ は affine・有限表示・平坦である。一方、粗空間の忘却射 $f:N_{n,d}\to M_{n,d}$ の平坦領域は、次の定理で完全に記述される。

$$
\boxed{\operatorname{Flat}(f)=f^{-1}(M_{n,d}^{\mathrm{sm}}).}
$$

これは両次数・全 $n\geq2$ に成り立つ。$N_{n,d}$ は Cohen–Macaulay であり、各粗ファイバーの**被約化**は $C_{d,n}/\operatorname{Aut}(X)$、その次元は上表の相対次元である。基底の粗空間が特異なら、その上では零 Poisson 構造を含むファイバー内の全ての点で非平坦となる。証明は `thm:coarse-flat-locus` にある。

### 自己同型と非被約ファイバー

**任意の固定した $X$ について、一般の非零 Poisson 構造は $\operatorname{Aut}(X,\pi)=1$ を満たす。** 射影化した一般の構造の安定化群は、次数2で $\mu_2$、次数1では $A_4\ne0$ で $\mu_2$、$A_4=0$ で $\mu_6$ となる。多様体自身が一般的であることは仮定しない。

次数1の $X:z^2-y^3-f_6(x)=0$ で $\operatorname{Aut}(X)=\mu_6$ となる模型を取ると、粗忘却射の非平坦性とファイバーの冪零構造を具体的に計算できる。$a=\binom{n+3}{4}$、$b=\binom{n+5}{6}-n^2$ として、零点での完成局所環は

$$
\mathbb C[[s_1,\ldots,s_b,u_1,\ldots,u_a]]^{\mu_3}
\longrightarrow
\mathbb C[[s,u,v_1,\ldots,v_n]]^{\mu_6},
\qquad (s,u,v)\mapsto(s,\zeta^2u,\zeta v).
$$

粗ファイバーの完成局所環は $(\mathbb C[[u,v]]/(u)^3)^{\mu_6}$ であり、$c=u_1v_1^4$ は $c^2\ne0$、$c^3=0$ を満たす。曲面では $a=5,b=3$、非平坦性を検出する階数1の共変加群の最小生成元数は15である。固定 $X$ の商の被約環だけでは、この粗ファイバーを記述できない。本文には一般次元の証明と、射影対称性のない明示的二変数六次形式を置く。

### 零切断、符号商、解消

次数1の Poisson スタック全体と、次数2の非零部分は滑らかである。次数2の $n\geq3$ では非滑らかな点の集合が零切断に一致し、多様体を動かしても零点での二次障害 $Q\wedge Q$ は消えない。曲面のスタックの次元は次数1・2で10・9、三次元では37・24となる。

次数2の零切断の blow-up は、相対 Grassmann 上の tautological $\mathcal O(-1)$ の全空間として記述される滑らかな DM スタックである。元の Plücker 錐は $n=3$ で五次元二次錐、$n\geq4$ で非局所完全交叉であり、$n\geq3$ では Gorenstein terminal、頂点 blow-up の discrepancy は $n$ である。

二重被覆対合は $\pi\mapsto-\pi$ と作用する。この対合だけを基底で除いた相対粗空間は、偶数 Veronese 錐 $C_{d,n}^{(2)}$ になる。一般多様体の自己同型群はちょうどこの $\mu_2$ なので、その開部分では全粗空間も étale 局所的に $S\times C_{d,n}^{(2)}$ となる。$S$ は滑らかである。

$Y=\mathbb P^{n-1}$ または $\operatorname{Gr}(2,n+1)$ とすると、符号商の頂点 blow-up は $\operatorname{Tot}\mathcal O_Y(-2)$。族では元の Poisson 表現の指標を含む線型化を保持して降下し、もとの解消は相対粗解消の例外因子に沿う二乗根スタックになる。

$$
\mathcal R\simeq\sqrt[2]{(\overline{\mathcal R},\overline E)},\qquad r^*\overline E=2E.
$$

符号商の標準指数は $2/\gcd(2,r)$、頂点 blow-up の discrepancy は $r/2-1$ であり、$r=n$（次数1）、$r=n+1$（次数2）。次数1曲面は $A_1$ で canonical・非terminal、それ以外の符号商は terminal となる。追加の自己同型を持つ全ての層の粗特異点まで分類したものではない。

### 相対構成と保持する成果

基本線束を選べる族 $p:\mathcal X\to T$ では、同変性を担う内在的な公式は

$$
p_*\bigwedge^2T_{\mathcal X/T}
\simeq\bigwedge^{n-1}(p_*H)\otimes
p_*(\omega_{\mathcal X/T}^{-1}\otimes H^{-(n-1)}).
$$

この束は $H$ を基底の線束で捻っても変わらず、基本線束自体の大域的存在を仮定せずに降下する。基本偏極の**クラス**は滑らかな族に一意に定まる。Poisson 構造の非零部を独立なスカラー倍で割ると、局所的な $\operatorname{Gr}_T(n-1,p_*H)$ の降下を得る。基本線束のスカラー自己同型、被覆対合、Poisson 構造のスカラー倍は区別する。

非零構造の一般階数は2。標準 ambient stack への一意な延長、一般の部分線型系の一般の葉の閉包として現れる del Pezzo 曲面、曲面の反標準退化因子、中心的超曲面の形式量子化、曲面 potential と条件付き AS 拡大についての有効な証明も本文に保持する。

## 公表原稿・証明の状態・次の課題

[poisson-del-pezzo.tex](papers/poisson-del-pezzo.tex) は、del Pezzo manifold の短いレビューから、固定対象の分類、葉の幾何、族、モジュライ、粗空間、特異性と解消、量子化へ進む。主原稿は本文を持ち、八つの分割ソースを読み込む。

今回の論理的点検は、新しい粗モジュライ・平坦領域・自己同型・明示的非被約例と、符号商・解消の議論を中心とする。既存の分類・族・量子化の本文を保持したことは、それらの全証明を今回再監査したという意味ではない。形式証明器による検証は行っていない。四つの厳密検算と48頁の LuaLaTeX 組版は成功しており、表示確認を含む個別の状態は [再現手順](docs/reproduction.md) に記す。

曲面の点分類、三次元の LPT の分類、Hong–Xu による曲面の変形次元10・9は既知である。粗空間と平坦領域の証明には Luna、有限群不変環、miracle flatness 等の一般論を使う。**任意次元・相対 Jacobi スキーム・粗忘却射への適用の新規性・優先権の包括的確認は未了。** 形式量子化には Kontsevich、曲面 potential には Etingof–Ginzburg の定理を用いる。一次資料と適用範囲は [文献メモ](research/literature_notes.md) に記載する。

次の主要課題は、次数2の特別な自己同型層と基底粗空間 $M_{n,2}$ の特異 locus の具体化、対応する粗ファイバーの冪零構造、相対量子化の同変降下である。特異な多様体を加えたコンパクト化、量子化の代数化、全非可換変形の網羅性も未解決として区別する。

## 原稿と研究資産

| ファイル | 役割 |
| --- | --- |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則、現在の到達点、証明の状態、次の着手方法 |
| [poisson-del-pezzo.tex](papers/poisson-del-pezzo.tex) | 日本語 LuaLaTeX の公表用主原稿 |
| [papers/sections/](papers/sections/) | レビュー・分類・幾何・族・モジュライ・粗空間・特異性・量子化の八つの本文ソース |
| [research/research_notes.md](research/research_notes.md) | 記法、証明の依存、同変性、明示模型、残る障害 |
| [research/dp4_comparison.md](research/dp4_comparison.md) | 次数4との比較、高階数の例、lift の非一意性、量子化模型 |
| [research/literature_notes.md](research/literature_notes.md)・[references.bib](references.bib) | 一次資料の版・箇所、書誌、既知性の確認範囲 |
| [computations/verify_jacobi.py](computations/verify_jacobi.py) | Casimir・Jacobi・Plücker 係数回収の厳密検算 |
| [computations/verify_families.py](computations/verify_families.py) | 座標変換の character と同時変形の二次障害 |
| [computations/verify_cone.py](computations/verify_cone.py) | 元の錐・符号商の次元、方程式数、記号恒等式、独立な tableau 数え上げ |
| [computations/verify_coarse.py](computations/verify_coarse.py) | 明示的六点配置の全120射影変換、共変加群の生成元数、粗ファイバーの冪零元 |
| [docs/reproduction.md](docs/reproduction.md) | 再生成・組版・検証の手順と確認範囲 |

```sh
python3 -m pip install -r requirements.txt
make verify
make pdf
```

ルートから `latexmk` だけでも主原稿をビルドできる。LuaLaTeX・LuaTeX-ja・BibTeX・latexmk と Noto CJK フォントを使用し、`build/poisson-del-pezzo.pdf` と SyncTeX を生成する。`.vscode/` に LaTeX Workshop の設定と拡張推奨を置く。PDF・中間生成物は Git で追跡しない。GitHub Actions は使わない。

GitHub `main` を正本とし、通常コミット・pushと research-hub の該当項目の更新を行う。定常的な Library への二重保存や ZIP 作成は行わず、push失敗時の緊急保存または明示的な依頼時に限る。対象repoの反映とhub更新は別々に確認する。

## 関連リポジトリとの分担

- **次数1・2の分類・族・モジュライ**：本リポジトリ。
- **次数3の一般次元 cubic hypersurface**：[nc-cubic](https://github.com/uedakazushi/nc-cubic)。既存の分類・量子化原稿を正本とする。
- **次数4の二次完全交叉**：[poisson-22ci](https://github.com/uedakazushi/poisson-22ci)、[nc-22ci](https://github.com/uedakazushi/nc-22ci)。本repoの比較ノートは詳細分類の代わりではない。
- **次数1の非可換圏の認識・モジュライ**：[nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)。Poisson 構造の量子化と、圏から ambient を認識する問題を区別する。
- **研究全体の入口**：[research-hub](https://github.com/uedakazushi/research-hub)。
