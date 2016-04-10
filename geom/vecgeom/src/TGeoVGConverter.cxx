// @(#)root/geomconverter:$Id:$
// Author: Mihaela Gheata   30/03/16
/*************************************************************************
 * Copyright (C) 1995-2000, Rene Brun and Fons Rademakers.               *
 * All rights reserved.                                                  *
 *                                                                       *
 * For the licensing terms see $ROOTSYS/LICENSE.                         *
 * For the list of contributors see $ROOTSYS/README/CREDITS.             *
 *************************************************************************/

//______________________________________________________________________________
// TGeoVGConverter - Geometry converter to VecGeom
//______________________________________________________________________________

#include "TGeoVGConverter.h"
#include "TGeoVGShape.h"

ClassImp(TGeoVGConverter)

////////////////////////////////////////////////////////////////////////////////
///*-*-*-*-*-*-*-*-*-*-*Geometry converter default constructor*-*-*-*-*-*-*-*-*
///*-*                  ====================================

TGeoVGConverter::TGeoVGConverter(TGeoManager *manager) : TVirtualGeoConverter(manager)
{
   TVirtualGeoConverter::SetConverter(this);
}

////////////////////////////////////////////////////////////////////////////////
///*-*-*-*-*-*-*-*-*-*-*Geometry converter default destructor*-*-*-*-*-*-*-*-*
///*-*                  ===================================

TGeoVGConverter::~TGeoVGConverter()
{
}

////////////////////////////////////////////////////////////////////////////////
///*-*-*-*-*-*-*-*-*-*-*Main geometry convertion method *-*-*-*-*-*-*-*-*
///*-*                  ===================================
void TGeoVGConverter::ConvertGeometry()
{
// Convert all geometry shapes connected to volumes to VecGeom shapes
   // First convert the top volume
   TGeoVolume *top = fGeom->GetTopVolume();
   TGeoVGShape *vgshape = TGeoVGShape::Create(top->GetShape());
   Int_t nconverted=0;
   // If shape of top volume not known by VecGeom, keep old one
   if (vgshape) {
      nconverted++;
      top->SetShape(vgshape);
   }
   // Now iterate the active geometry tree
   TGeoIterator next(fGeom->GetTopVolume());
   TGeoNode *node;
   while ((node = next.Next())) {
      TGeoVolume *vol = node->GetVolume();
      // If shape not already converted, convert it
      if ( vol->GetShape()->IsA() != TGeoVGShape::Class() ) {
         // printf("Converting %s\n", vol->GetName());
         vgshape = TGeoVGShape::Create(vol->GetShape());
         if (vgshape) {
            nconverted++;
            vol->SetShape(vgshape);
         }
      }
   }
   printf("# Converted %d shapes to VecGeom ones\n", nconverted);
}
