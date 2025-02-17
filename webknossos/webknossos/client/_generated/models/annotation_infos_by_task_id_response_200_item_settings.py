from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.annotation_infos_by_task_id_response_200_item_settings_resolution_restrictions import (
    AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationInfosByTaskIdResponse200ItemSettings")


@attr.s(auto_attribs=True)
class AnnotationInfosByTaskIdResponse200ItemSettings:
    """ """

    allowed_modes: Union[Unset, List[str]] = UNSET
    branch_points_allowed: Union[Unset, int] = UNSET
    soma_clicking_allowed: Union[Unset, int] = UNSET
    volume_interpolation_allowed: Union[Unset, int] = UNSET
    merger_mode: Union[Unset, int] = UNSET
    resolution_restrictions: Union[
        Unset, AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_modes, Unset):
            allowed_modes = self.allowed_modes

        branch_points_allowed = self.branch_points_allowed
        soma_clicking_allowed = self.soma_clicking_allowed
        volume_interpolation_allowed = self.volume_interpolation_allowed
        merger_mode = self.merger_mode
        resolution_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolution_restrictions, Unset):
            resolution_restrictions = self.resolution_restrictions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_modes is not UNSET:
            field_dict["allowedModes"] = allowed_modes
        if branch_points_allowed is not UNSET:
            field_dict["branchPointsAllowed"] = branch_points_allowed
        if soma_clicking_allowed is not UNSET:
            field_dict["somaClickingAllowed"] = soma_clicking_allowed
        if volume_interpolation_allowed is not UNSET:
            field_dict["volumeInterpolationAllowed"] = volume_interpolation_allowed
        if merger_mode is not UNSET:
            field_dict["mergerMode"] = merger_mode
        if resolution_restrictions is not UNSET:
            field_dict["resolutionRestrictions"] = resolution_restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_modes = cast(List[str], d.pop("allowedModes", UNSET))

        branch_points_allowed = d.pop("branchPointsAllowed", UNSET)

        soma_clicking_allowed = d.pop("somaClickingAllowed", UNSET)

        volume_interpolation_allowed = d.pop("volumeInterpolationAllowed", UNSET)

        merger_mode = d.pop("mergerMode", UNSET)

        _resolution_restrictions = d.pop("resolutionRestrictions", UNSET)
        resolution_restrictions: Union[
            Unset, AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions
        ]
        if isinstance(_resolution_restrictions, Unset):
            resolution_restrictions = UNSET
        else:
            resolution_restrictions = AnnotationInfosByTaskIdResponse200ItemSettingsResolutionRestrictions.from_dict(
                _resolution_restrictions
            )

        annotation_infos_by_task_id_response_200_item_settings = cls(
            allowed_modes=allowed_modes,
            branch_points_allowed=branch_points_allowed,
            soma_clicking_allowed=soma_clicking_allowed,
            volume_interpolation_allowed=volume_interpolation_allowed,
            merger_mode=merger_mode,
            resolution_restrictions=resolution_restrictions,
        )

        annotation_infos_by_task_id_response_200_item_settings.additional_properties = d
        return annotation_infos_by_task_id_response_200_item_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
