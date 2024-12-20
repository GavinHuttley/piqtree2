from piqtree2.model._freq_type import FreqType, get_freq_type
from piqtree2.model._rate_type import RateModel, get_rate_type
from piqtree2.model._substitution_model import SubstitutionModel, get_substitution_model


class Model:
    """Specification for substitution models.

    Stores the substitution model with base frequency settings.
    """

    def __init__(
        self,
        submod_type: str | SubstitutionModel,
        freq_type: str | FreqType | None = None,
        rate_model: str | RateModel | None = None,
        *,
        invariant_sites: bool = False,
    ) -> None:
        """Construct Model class.

        Parameters
        ----------
        submod_type : str | SubstitutionModel
            The substitution model to use
        freq_type : str | FreqType | None, optional
            State frequency specification, by default None. (defaults
            to empirical base frequencies if not specified by model).
        rate_model : str | RateModel | None, optional
            Rate heterogeneity across sites model, by default
            no Gamma, and no FreeRate.
        invariant_sites : bool, optional
            Invariable sites, by default False.

        """
        self.submod_type = get_substitution_model(submod_type)
        self.freq_type = get_freq_type(freq_type) if freq_type else None
        self.rate_type = (
            get_rate_type(rate_model, invariant_sites=invariant_sites)
            if rate_model is not None or invariant_sites
            else None
        )

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        attrs = [
            f"submod_type={getattr(self.submod_type, 'name', None)}",
            f"freq_type={getattr(self.freq_type, 'name', None)}",
            f"rate_type={getattr(self.rate_type, 'name', None)}",
        ]
        return f"Model({', '.join(attrs)})"

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.

        """
        iqtree_extra_args = (
            x for x in (self.freq_type, self.rate_type) if x is not None
        )
        return "+".join(x.iqtree_str() for x in [self.submod_type, *iqtree_extra_args])

    @property
    def rate_model(self) -> RateModel | None:
        """The RateModel used, if one is chosen.

        Returns
        -------
        RateModel | None
            The RateModel used by the Model.

        """
        return self.rate_type.rate_model if self.rate_type else None

    @property
    def invariant_sites(self) -> bool:
        """Whether invariant sites are used.

        Returns
        -------
        bool
            True if invariant sites are used by the model, False otherwise.

        """
        return self.rate_type.invariant_sites if self.rate_type else False
