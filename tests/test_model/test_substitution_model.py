import re

import pytest

from piqtree.model import AaModel, DnaModel, SubstitutionModel, get_substitution_model


@pytest.mark.parametrize("model_class", [DnaModel, AaModel])
def test_number_of_descriptions(
    model_class: type[DnaModel] | type[AaModel],
) -> None:
    assert len(model_class) == len(model_class._descriptions())


@pytest.mark.parametrize("model_class", [DnaModel, AaModel])
def test_descriptions_exist(model_class: type[DnaModel] | type[AaModel]) -> None:
    for model in model_class:
        # Raises an error if description not present
        _ = model.description


@pytest.mark.parametrize(
    ("model_class", "model_type"),
    [(DnaModel, "nucleotide"), (AaModel, "protein")],
)
def test_model_type(
    model_class: type[DnaModel] | type[AaModel],
    model_type: str,
) -> None:
    assert model_class.model_type() == model_type

    for model in model_class:
        assert model.model_type() == model_type


@pytest.mark.parametrize(
    ("submod_type", "iqtree_str"),
    [
        (DnaModel.F81, "F81"),
        (DnaModel.LIE_10_34, "10.34"),
        (AaModel.NQ_insect, "NQ.insect"),
        ("NQ.yeast", "NQ.yeast"),
        ("GTR", "GTR"),
        ("2.2b", "2.2b"),
    ],
)
def test_get_substitution_model(
    submod_type: SubstitutionModel | str,
    iqtree_str: str,
) -> None:
    out = get_substitution_model(submod_type)
    assert isinstance(out, SubstitutionModel)
    assert out.iqtree_str() == iqtree_str


@pytest.mark.parametrize(
    "submod_type",
    ["FQ", "F", "+GTR", "AA", "G8", ""],
)
def test_invalid_substitution_model(submod_type: str) -> None:
    with pytest.raises(
        ValueError,
        match=re.escape(f"Unknown substitution model: {submod_type!r}"),
    ):
        _ = get_substitution_model(submod_type)
