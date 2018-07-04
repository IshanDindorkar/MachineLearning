## Copyright (C) 2018 ishan
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} costFunction (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: ishan <ishan@DESKTOP-MPKV0F8>
## Created: 2018-07-04

function J = costFunction (X, y, theta)
  % X is the matrix of training examples
  % y is the class labels
  
  m = size(X, 1);
  predictions = X * theta;
  sqrErrors = (predictions - y).^2;
 
  J = 1/(2*m) * sum(sqrErrors); 

endfunction
